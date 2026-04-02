from __future__ import annotations

import uuid
from pathlib import Path


def make_test_dir(name: str) -> Path:
    root = Path(__file__).resolve().parent / ".artifacts"
    root.mkdir(exist_ok=True)
    target = root / f"{name}_{uuid.uuid4().hex[:8]}"
    target.mkdir(parents=True, exist_ok=True)
    return target
