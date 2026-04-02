from datetime import datetime, timezone
from pathlib import Path

from fastapi.testclient import TestClient

from transcriber.core.models import TranscriptionResult
from transcriber.web import app as app_module


class FakeEngine:
    def transcribe(self, request, progress_callback=None):
        if progress_callback:
            progress_callback(type("Event", (), {"stage": "running", "message": "working", "percent": 50})())
            progress_callback(type("Event", (), {"stage": "completed", "message": "done", "percent": 100})())

        output_path = request.input_path.with_suffix(".txt")
        output_path.write_text("hello", encoding="utf-8")

        return TranscriptionResult(
            status="success",
            transcript_path=output_path,
            source_path=request.input_path,
            model_used=request.model or "whisper-large-v3",
            chunk_count=1,
            started_at=datetime.now(timezone.utc),
            finished_at=datetime.now(timezone.utc),
            duration_sec=0.2,
            metadata={},
            error=None,
        )


def test_api_job_lifecycle(monkeypatch):
    monkeypatch.setattr(app_module, "engine", FakeEngine())
    client = TestClient(app_module.app)

    resp = client.post(
        "/api/transcriptions",
        files={"file": ("sample.wav", b"audio-data", "audio/wav")},
        data={"model": "whisper-large-v3"},
    )
    assert resp.status_code == 200
    job_id = resp.json()["job_id"]

    for _ in range(20):
        status_resp = client.get(f"/api/transcriptions/{job_id}")
        payload = status_resp.json()
        if payload["status"] in {"completed", "failed"}:
            break
    else:
        raise AssertionError("Job did not complete in time")

    assert payload["status"] == "completed"
    assert payload["result"]["status"] == "success"
