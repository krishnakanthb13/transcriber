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

    kwargs = {"api_key": api_key}
    
    if default_model := os.getenv("TRANSCRIBER_MODEL"):
        kwargs["default_model"] = default_model.strip()
        
    if max_upload_mb := os.getenv("TRANSCRIBER_MAX_UPLOAD_MB"):
        kwargs["max_upload_mb"] = int(max_upload_mb)
        
    if chunk_duration := os.getenv("TRANSCRIBER_CHUNK_DURATION_SECONDS"):
        kwargs["chunk_duration_seconds"] = int(chunk_duration)
        
    if chunk_overlap := os.getenv("TRANSCRIBER_CHUNK_OVERLAP_SECONDS"):
        kwargs["chunk_overlap_seconds"] = int(chunk_overlap)
        
    if max_retries := os.getenv("TRANSCRIBER_MAX_RETRIES"):
        kwargs["max_retries"] = int(max_retries)
        
    if log_file_raw := os.getenv("TRANSCRIBER_LOG_FILE"):
        kwargs["log_file"] = Path(log_file_raw.strip()) if log_file_raw.strip().upper() != "OFF" else None

    config = TranscriptionConfig(**kwargs)
    return Settings(config=config)
