from __future__ import annotations

import difflib
import tempfile
import time
from collections.abc import Callable
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from .audio import inspect_audio, load_segment
from .chunking import build_chunk_plan
from .groq_client import GroqTranscriptionClient
from .logging_utils import configure_logger
from .models import ProgressEvent, TranscriptionConfig, TranscriptionRequest, TranscriptionResult

ProgressCallback = Callable[[ProgressEvent], None]


class TranscriptionEngine:
    def __init__(
        self,
        config: TranscriptionConfig,
        client: GroqTranscriptionClient | None = None,
        verbose: bool = False,
    ) -> None:
        self.config = config
        self.client = client or GroqTranscriptionClient(api_key=config.api_key)
        self.logger = configure_logger(config.log_file, verbose=verbose)

    def transcribe(
        self,
        request: TranscriptionRequest,
        progress_callback: ProgressCallback | None = None,
    ) -> TranscriptionResult:
        started_at = datetime.now(tz=timezone.utc)
        input_path = request.input_path.expanduser().resolve()
        model = request.model or self.config.default_model

        def emit(stage: str, message: str, percent: int) -> None:
            if progress_callback:
                progress_callback(ProgressEvent(stage=stage, message=message, percent=percent))

        try:
            emit("validating", "Validating audio input", 5)
            audio_info = inspect_audio(input_path, self.config.allowed_extensions)
            self.logger.info(
                "transcription_started file=%s size=%s model=%s",
                audio_info.path,
                audio_info.file_size,
                model,
            )

            output_path = self._resolve_output_path(audio_info.path, request.output_path)

            transcript_parts: list[str] = []
            metadata: dict[str, object] = {
                "file_name": audio_info.path.name,
                "file_size_bytes": audio_info.file_size,
                "duration_seconds": audio_info.duration_seconds,
                "model": model,
                "chunks": [],
            }

            chunk_plan = build_chunk_plan(
                file_size=audio_info.file_size,
                duration_seconds=audio_info.duration_seconds,
                max_upload_bytes=self.config.max_upload_bytes,
                preferred_chunk_duration_seconds=self.config.chunk_duration_seconds,
                overlap_seconds=self.config.chunk_overlap_seconds,
            )

            if chunk_plan.chunk_count == 1:
                emit("transcribing", "Transcribing audio", 30)
                response = self.client.transcribe_file(audio_info.path, model=model)
                transcript_parts.append(response["text"].strip())
                metadata["chunks"].append({"index": 1, "source": str(audio_info.path), **response})
            else:
                emit("preparing", f"Preparing {chunk_plan.chunk_count} chunks", 15)
                segment = load_segment(audio_info.path)
                stride_ms = chunk_plan.stride_seconds * 1000
                chunk_ms = chunk_plan.chunk_duration_seconds * 1000

                with tempfile.TemporaryDirectory(prefix="transcriber_chunks_") as tmp_dir:
                    tmp_root = Path(tmp_dir)
                    for idx in range(chunk_plan.chunk_count):
                        start_ms = idx * stride_ms
                        end_ms = min(len(segment), start_ms + chunk_ms)
                        chunk_segment = segment[start_ms:end_ms]

                        chunk_path = tmp_root / f"chunk_{idx + 1:03d}.mp3"
                        chunk_segment.export(chunk_path, format="mp3", bitrate="64k")

                        percent = 20 + int(((idx + 1) / chunk_plan.chunk_count) * 70)
                        emit(
                            "transcribing",
                            f"Transcribing chunk {idx + 1}/{chunk_plan.chunk_count}",
                            min(percent, 90),
                        )
                        
                        response = None
                        last_error = None
                        for attempt in range(max(1, self.config.max_retries)):
                            try:
                                response = self.client.transcribe_file(chunk_path, model=model)
                                break
                            except Exception as e:
                                last_error = e
                                self.logger.warning("Chunk %d retry %d due to error: %s", idx + 1, attempt + 1, e)
                                time.sleep(2 ** attempt)
                        
                        if response is None:
                            raise RuntimeError(f"Chunk transcription failed after {self.config.max_retries} retries: {last_error}")

                        transcript_parts.append(response["text"].strip())
                        metadata["chunks"].append(
                            {
                                "index": idx + 1,
                                "start_ms": start_ms,
                                "end_ms": end_ms,
                                "source": str(chunk_path),
                                **response,
                            }
                        )

            emit("merging", "Combining transcript segments", 95)
            transcript_text = self._merge_transcript_parts(transcript_parts)
            output_path.write_text(transcript_text, encoding="utf-8")

            finished_at = datetime.now(tz=timezone.utc)
            result = TranscriptionResult(
                status="success",
                transcript_path=output_path,
                source_path=audio_info.path,
                model_used=model,
                chunk_count=chunk_plan.chunk_count,
                started_at=started_at,
                finished_at=finished_at,
                duration_sec=(finished_at - started_at).total_seconds(),
                metadata=metadata,
                error=None,
            )
            self.logger.info("transcription_completed payload=%s", asdict(result))
            emit("completed", "Transcription complete", 100)
            return result
        except Exception as exc:
            finished_at = datetime.now(tz=timezone.utc)
            self.logger.error("transcription_failed file=%s error=%s", input_path, exc)
            emit("failed", f"Transcription failed: {exc}", 100)
            return TranscriptionResult(
                status="failed",
                transcript_path=None,
                source_path=input_path,
                model_used=model,
                chunk_count=0,
                started_at=started_at,
                finished_at=finished_at,
                duration_sec=(finished_at - started_at).total_seconds(),
                metadata={},
                error=str(exc),
            )

    def _resolve_output_path(self, input_path: Path, requested_output: Path | None) -> Path:
        if requested_output:
            output_path = requested_output.expanduser().resolve()
            if output_path.suffix.lower() != ".txt":
                output_path = output_path.with_suffix(".txt")
        else:
            output_path = input_path.with_suffix(".txt")

        if output_path.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = output_path.with_stem(f"{output_path.stem}_{timestamp}")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        return output_path

    def _merge_transcript_parts(self, parts: list[str]) -> str:
        if not parts:
            return ""
        
        merged_text = parts[0]
        for next_part in parts[1:]:
            if not next_part:
                continue
                
            search_len = min(400, len(merged_text), len(next_part))
            if search_len > 10:
                end_of_t1 = merged_text[-search_len:]
                start_of_t2 = next_part[:search_len]
                
                matcher = difflib.SequenceMatcher(None, end_of_t1, start_of_t2)
                match = matcher.find_longest_match(0, len(end_of_t1), 0, len(start_of_t2))
                
                if match.size > 15:
                    merged_text = merged_text + " " + next_part[match.b + match.size:].lstrip()
                    continue
            
            merged_text = merged_text + "\n\n" + next_part
            
        return merged_text
