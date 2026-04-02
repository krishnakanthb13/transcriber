#!/usr/bin/env bash
set -euo pipefail

NAUTILUS_SCRIPT="$HOME/.local/share/nautilus/scripts/Transcribe Audio"
if [ -f "$NAUTILUS_SCRIPT" ]; then
  rm "$NAUTILUS_SCRIPT"
  echo "Removed Nautilus script"
else
  echo "Nautilus script not found"
fi
