#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: transcribe-audio.sh <audio-file>"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

if [ -x "$REPO_ROOT/.venv/bin/transcribe" ]; then
  "$REPO_ROOT/.venv/bin/transcribe" "$1"
else
  transcribe "$1"
fi
