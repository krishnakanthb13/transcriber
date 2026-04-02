from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from .models import TranscriptionConfig


@dataclass(slots=True)
class Settings:
    config: TranscriptionConfig


def load_settings() -> Settings:
    load_dotenv()

    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        raise ValueError("GROQ_API_KEY is required. Set it in your environment or .env file.")

    default_model = os.getenv("TRANSCRIBER_MODEL", "whisper-large-v3").strip()
    max_upload_mb = int(os.getenv("TRANSCRIBER_MAX_UPLOAD_MB", "25"))
    chunk_duration_seconds = int(os.getenv("TRANSCRIBER_CHUNK_DURATION_SECONDS", "600"))
    
    log_file_raw = os.getenv("TRANSCRIBER_LOG_FILE", "logs/transcriber.log").strip()
    log_file = Path(log_file_raw) if log_file_raw and log_file_raw.upper() != "OFF" else None

    config = TranscriptionConfig(
        api_key=api_key,
        default_model=default_model,
        max_upload_mb=max_upload_mb,
        chunk_duration_seconds=chunk_duration_seconds,
        log_file=log_file,
    )
    return Settings(config=config)
