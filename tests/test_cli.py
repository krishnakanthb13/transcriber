from pathlib import Path

from transcriber.cli.main import main
from transcriber.core.models import TranscriptionResult
from tests.helpers import make_test_dir


class FakeEngine:
    def __init__(self, *args, **kwargs):
        pass

    def transcribe(self, request, progress_callback=None):
        if progress_callback:
            progress_callback(type("Event", (), {"percent": 50, "stage": "transcribing", "message": "working"})())
        return TranscriptionResult(
            status="success",
            transcript_path=Path("out.txt"),
            source_path=request.input_path,
            model_used=request.model or "whisper-large-v3",
            chunk_count=1,
            started_at=__import__("datetime").datetime.now(__import__("datetime").timezone.utc),
            finished_at=__import__("datetime").datetime.now(__import__("datetime").timezone.utc),
            duration_sec=1.0,
            metadata={},
            error=None,
        )


class FakeSettings:
    def __init__(self):
        self.config = object()


def test_cli_transcribe_success(monkeypatch, capsys):
    tmp_path = make_test_dir("cli")
    file_path = tmp_path / "a.wav"
    file_path.write_bytes(b"x")

    monkeypatch.setattr("transcriber.cli.main.load_settings", lambda: FakeSettings())
    monkeypatch.setattr("transcriber.cli.main.TranscriptionEngine", FakeEngine)

    rc = main(["transcribe", str(file_path)])
    out = capsys.readouterr().out

    assert rc == 0
    assert "Transcript saved to:" in out
