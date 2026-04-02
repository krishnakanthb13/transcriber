from __future__ import annotations

import tempfile
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
from pathlib import Path
from threading import Lock

import uvicorn
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from transcriber.core import ProgressEvent, TranscriptionEngine, TranscriptionRequest, load_settings


@dataclass(slots=True)
class JobState:
    job_id: str
    status: str
    progress: dict
    result: dict | None = None
    error: str | None = None


class JobStore:
    def __init__(self) -> None:
        self._jobs: dict[str, JobState] = {}
        self._lock = Lock()

    def create(self) -> JobState:
        job = JobState(
            job_id=str(uuid.uuid4()),
            status="queued",
            progress={"stage": "queued", "message": "Queued", "percent": 0},
        )
        with self._lock:
            self._jobs[job.job_id] = job
        return job

    def update(self, job_id: str, *, status: str | None = None, progress: dict | None = None, result: dict | None = None, error: str | None = None) -> None:
        with self._lock:
            job = self._jobs[job_id]
            if status is not None:
                job.status = status
            if progress is not None:
                job.progress = progress
            if result is not None:
                job.result = result
            if error is not None:
                job.error = error

    def get(self, job_id: str) -> JobState | None:
        with self._lock:
            return self._jobs.get(job_id)


job_store = JobStore()
executor = ThreadPoolExecutor(max_workers=2)
engine: TranscriptionEngine | None = None

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Transcriber Web")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/api/transcriptions")
async def create_transcription(
    file: UploadFile = File(...),
    model: str | None = Form(default=None),
) -> dict:
    upload_dir = Path(tempfile.gettempdir()) / "transcriber_uploads"
    upload_dir.mkdir(parents=True, exist_ok=True)

    suffix = Path(file.filename or "audio").suffix or ".tmp"
    upload_path = upload_dir / f"{uuid.uuid4()}{suffix}"
    upload_path.write_bytes(await file.read())

    job = job_store.create()
    job_store.update(
        job.job_id,
        progress={"stage": "queued", "message": "Upload complete; waiting for worker", "percent": 5},
    )

    executor.submit(_run_job, job.job_id, upload_path, model)
    return {"job_id": job.job_id, "status": job.status, "progress": job.progress}


@app.get("/api/transcriptions/{job_id}")
def get_transcription(job_id: str) -> dict:
    job = job_store.get(job_id)
    if not job:
        return {"error": "Job not found", "status": "missing"}

    return {
        "job_id": job.job_id,
        "status": job.status,
        "progress": job.progress,
        "result": job.result,
        "error": job.error,
    }


def _run_job(job_id: str, upload_path: Path, model: str | None) -> None:
    global engine
    if engine is None:
        settings = load_settings()
        engine = TranscriptionEngine(config=settings.config)

    def on_progress(event: ProgressEvent) -> None:
        job_store.update(
            job_id,
            status="running" if event.stage not in {"completed", "failed"} else event.stage,
            progress={"stage": event.stage, "message": event.message, "percent": event.percent},
        )

    try:
        result = engine.transcribe(
            TranscriptionRequest(input_path=upload_path, output_path=None, model=model),
            progress_callback=on_progress,
        )

        result_dict = asdict(result)
        # Include transcript text in the API response so the web UI can display it
        if result.status == "success" and result.transcript_path and result.transcript_path.exists():
            result_dict["transcript_text"] = result.transcript_path.read_text(encoding="utf-8")

        if result.status == "success":
            job_store.update(job_id, status="completed", result=result_dict, progress={"stage": "completed", "message": "Done", "percent": 100})
        else:
            job_store.update(job_id, status="failed", error=result.error, result=result_dict, progress={"stage": "failed", "message": result.error or "Failed", "percent": 100})
    finally:
        upload_path.unlink(missing_ok=True)


def run() -> None:
    uvicorn.run("transcriber.web.app:app", host="127.0.0.1", port=3004, reload=False)


if __name__ == "__main__":
    run()

