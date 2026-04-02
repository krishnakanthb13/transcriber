$ErrorActionPreference = "Stop"

python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\pip install -e ".[dev]"

Write-Host "Environment setup complete."
