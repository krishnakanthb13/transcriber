from transcriber.core.chunking import build_chunk_plan


def test_chunk_plan_single_chunk_when_within_limit():
    plan = build_chunk_plan(
        file_size=1_000_000,
        duration_seconds=120,
        max_upload_bytes=25 * 1024 * 1024,
        preferred_chunk_duration_seconds=600,
    )
    assert plan.chunk_count == 1


def test_chunk_plan_multiple_chunks_when_over_limit():
    plan = build_chunk_plan(
        file_size=150 * 1024 * 1024,
        duration_seconds=3600,
        max_upload_bytes=25 * 1024 * 1024,
        preferred_chunk_duration_seconds=600,
    )
    assert plan.chunk_count > 1
    assert plan.chunk_duration_seconds <= 600
