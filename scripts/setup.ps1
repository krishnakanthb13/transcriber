$ErrorActionPreference = "Stop"

py -3 -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\pip install -e ".[dev]"

Write-Host "Environment setup complete."
