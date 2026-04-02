from __future__ import annotations

from pathlib import Path
from typing import Any

from groq import Groq


class GroqTranscriptionClient:
    def __init__(self, api_key: str) -> None:
        self._client = Groq(api_key=api_key)

    def transcribe_file(self, audio_path: Path, model: str) -> dict[str, Any]:
        with audio_path.open("rb") as fh:
            response = self._client.audio.transcriptions.create(
                file=(audio_path.name, fh.read()),
                model=model,
                response_format="verbose_json",
            )

        text = getattr(response, "text", None)
        duration = getattr(response, "duration", None)
        language = getattr(response, "language", None)

        if isinstance(response, dict):
            text = response.get("text", text)
            duration = response.get("duration", duration)
            language = response.get("language", language)

        return {
            "text": text or "",
            "duration": duration,
            "language": language,
        }
