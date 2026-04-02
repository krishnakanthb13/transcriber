from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from pydub import AudioSegment


@dataclass(slots=True)
class AudioInfo:
    path: Path
    extension: str
    file_size: int
    duration_seconds: float


class AudioValidationError(ValueError):
    """Raised when audio file validation fails."""


def inspect_audio(path: Path, allowed_extensions: tuple[str, ...]) -> AudioInfo:
    if not path.exists() or not path.is_file():
        raise AudioValidationError(f"Audio file does not exist: {path}")

    extension = path.suffix.lower()
    if extension not in allowed_extensions:
        raise AudioValidationError(
            f"Unsupported audio format '{extension}'. Allowed: {', '.join(allowed_extensions)}"
        )

    segment = AudioSegment.from_file(path)
    duration_seconds = len(segment) / 1000.0

    return AudioInfo(
        path=path,
        extension=extension,
        file_size=path.stat().st_size,
        duration_seconds=duration_seconds,
    )


def load_segment(path: Path) -> AudioSegment:
    return AudioSegment.from_file(path)
