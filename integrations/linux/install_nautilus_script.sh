#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NAUTILUS_DIR="$HOME/.local/share/nautilus/scripts"

mkdir -p "$NAUTILUS_DIR"
cp "$SCRIPT_DIR/transcribe-audio.sh" "$NAUTILUS_DIR/Transcribe Audio"
chmod +x "$NAUTILUS_DIR/Transcribe Audio"

echo "Installed Nautilus script at: $NAUTILUS_DIR/Transcribe Audio"
