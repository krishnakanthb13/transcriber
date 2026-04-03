from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class TranscriptionConfig:
    api_key: str
    default_model: str = "whisper-large-v3"
    max_upload_mb: int = 25
    chunk_duration_seconds: int = 600
    
    # Determines the overlap window in seconds between chunks to ensure seamless text merging
    chunk_overlap_seconds: int = 5
    
    # Controls the maximum number of times to retry transcribing a chunk if the API request fails
    max_retries: int = 3
    
    log_file: Path | None = Path("logs/transcriber.log")
    allowed_extensions: tuple[str, ...] = (
        ".mp3",
        ".wav",
        ".m4a",
        ".flac",
        ".ogg",
        ".aac",
        ".wma",
        ".mp4",
        ".mpeg",
    )

    @property
    def max_upload_bytes(self) -> int:
        return self.max_upload_mb * 1024 * 1024


@dataclass(slots=True)
class TranscriptionRequest:
    input_path: Path
    output_path: Path | None = None
    model: str | None = None


@dataclass(slots=True)
class ProgressEvent:
    stage: str
    message: str
    percent: int


@dataclass(slots=True)
class TranscriptionResult:
    status: str
    transcript_path: Path | None
    source_path: Path
    model_used: str
    chunk_count: int
    started_at: datetime
    finished_at: datetime
    duration_sec: float
    metadata: dict[str, Any] = field(default_factory=dict)
    error: str | None = None
