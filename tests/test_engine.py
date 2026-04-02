from pathlib import Path

from transcriber.core.audio import AudioInfo
from transcriber.core.chunking import ChunkPlan
from transcriber.core.engine import TranscriptionEngine
from transcriber.core.models import TranscriptionConfig, TranscriptionRequest
from tests.helpers import make_test_dir


class FakeClient:
    def transcribe_file(self, audio_path: Path, model: str):
        return {"text": f"text-from-{audio_path.name}", "duration": 1.0, "language": "en"}


def test_engine_writes_timestamped_output_when_target_exists(monkeypatch):
    tmp_path = make_test_dir("engine_success")
    input_path = tmp_path / "sample.wav"
    input_path.write_bytes(b"fake-audio")
    existing_output = tmp_path / "sample.txt"
    existing_output.write_text("old", encoding="utf-8")

    monkeypatch.setattr(
        "transcriber.core.engine.inspect_audio",
        lambda *_args, **_kwargs: AudioInfo(
            path=input_path,
            extension=".wav",
            file_size=10,
            duration_seconds=30.0,
        ),
    )
    monkeypatch.setattr(
        "transcriber.core.engine.build_chunk_plan",
        lambda **_kwargs: ChunkPlan(chunk_count=1, chunk_duration_seconds=30),
    )

    config = TranscriptionConfig(api_key="test", log_file=tmp_path / "logs/app.log")
    engine = TranscriptionEngine(config=config, client=FakeClient())

    result = engine.transcribe(TranscriptionRequest(input_path=input_path))

    assert result.status == "success"
    assert result.transcript_path is not None
    assert result.transcript_path.exists()
    assert result.transcript_path.name != "sample.txt"
    assert "text-from-sample.wav" in result.transcript_path.read_text(encoding="utf-8")


def test_engine_returns_failed_result_on_exception(monkeypatch):
    tmp_path = make_test_dir("engine_failure")
    input_path = tmp_path / "missing.wav"

    def raise_error(*_args, **_kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr("transcriber.core.engine.inspect_audio", raise_error)

    config = TranscriptionConfig(api_key="test", log_file=tmp_path / "logs/app.log")
    engine = TranscriptionEngine(config=config, client=FakeClient())

    result = engine.transcribe(TranscriptionRequest(input_path=input_path))

    assert result.status == "failed"
    assert result.error is not None
