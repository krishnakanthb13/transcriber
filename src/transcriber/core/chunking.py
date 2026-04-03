from __future__ import annotations

from dataclasses import dataclass
from math import ceil


@dataclass(slots=True)
class ChunkPlan:
    chunk_count: int
    chunk_duration_seconds: int
    overlap_seconds: int
    stride_seconds: int


def build_chunk_plan(
    file_size: int,
    duration_seconds: float,
    max_upload_bytes: int,
    preferred_chunk_duration_seconds: int,
    overlap_seconds: int = 0,
) -> ChunkPlan:
    if file_size <= max_upload_bytes or duration_seconds <= 0:
        return ChunkPlan(
            chunk_count=1,
            chunk_duration_seconds=max(1, int(duration_seconds) or 1),
            overlap_seconds=0,
            stride_seconds=max(1, int(duration_seconds) or 1),
        )

    bytes_per_second = file_size / duration_seconds
    max_safe_seconds = int((max_upload_bytes / bytes_per_second) * 0.9)
    max_safe_seconds = max(30, max_safe_seconds)
    chunk_duration = min(preferred_chunk_duration_seconds, max_safe_seconds)

    # Calculate actual progression per chunk (stride)
    stride_seconds = max(1, chunk_duration - overlap_seconds)

    # To cover duration_seconds with overlapping chunks, we see how many strides it takes after the first overlap
    if duration_seconds <= chunk_duration:
        chunk_count = 1
    else:
        chunk_count = ceil((duration_seconds - overlap_seconds) / stride_seconds)

    return ChunkPlan(
        chunk_count=chunk_count,
        chunk_duration_seconds=chunk_duration,
        overlap_seconds=overlap_seconds,
        stride_seconds=stride_seconds,
    )
