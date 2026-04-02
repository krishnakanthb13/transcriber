from transcriber.core.settings import load_settings

from tests.helpers import make_test_dir

def test_load_settings_from_env(monkeypatch):
    tmp_path = make_test_dir("settings")
    monkeypatch.setenv("GROQ_API_KEY", "test-key")
    monkeypatch.setenv("TRANSCRIBER_MODEL", "whisper-large-v3-turbo")
    monkeypatch.setenv("TRANSCRIBER_MAX_UPLOAD_MB", "100")
    monkeypatch.setenv("TRANSCRIBER_CHUNK_DURATION_SECONDS", "300")
    monkeypatch.setenv("TRANSCRIBER_LOG_FILE", str(tmp_path / "app.log"))

    settings = load_settings()

    assert settings.config.api_key == "test-key"
    assert settings.config.default_model == "whisper-large-v3-turbo"
    assert settings.config.max_upload_mb == 100
    assert settings.config.chunk_duration_seconds == 300
    assert settings.config.log_file.name == "app.log"


def test_load_settings_requires_api_key(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    monkeypatch.setattr("transcriber.core.settings.load_dotenv", lambda: None)

    try:
        load_settings()
    except ValueError as exc:
        assert "GROQ_API_KEY" in str(exc)
    else:
        raise AssertionError("Expected ValueError when GROQ_API_KEY is missing")
