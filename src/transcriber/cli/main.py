from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from transcriber.core import TranscriptionEngine, TranscriptionRequest, load_settings


class Colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="transcribe",
        description="🚀 Transcribe local audio files using Groq Whisper API",
        epilog="Examples: transcribe audio.mp3 | transcribe audio.wav --model whisper-large-v3-turbo --verbose"
    )
    parser.add_argument("file_path", type=Path, help="Path to the source audio file")
    parser.add_argument("--model", default=None, help="Groq model (default: whisper-large-v3)")
    parser.add_argument("--output", type=Path, default=None, help="Optional custom output .txt path")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose debug logging")
    parser.add_argument("--json", action="store_true", help="Output full result as JSON")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        settings = load_settings()
    except Exception as e:
        print(f"{Colors.RED}[ERROR]{Colors.END} {e}")
        return 1

    engine = TranscriptionEngine(config=settings.config, verbose=args.verbose)

    def on_progress(event) -> None:
        # Simple colorful progress line
        pct_color = Colors.CYAN if event.percent < 100 else Colors.GREEN
        print(f"{Colors.BOLD}[{pct_color}{event.percent:>3}%{Colors.END}{Colors.BOLD}]{Colors.END} {Colors.YELLOW}{event.stage:<12}{Colors.END} {event.message}")

    print(f"{Colors.BOLD}--- Transcribing: {Colors.CYAN}{args.file_path.name}{Colors.END}{Colors.BOLD} ---{Colors.END}")
    
    result = engine.transcribe(
        TranscriptionRequest(input_path=args.file_path, output_path=args.output, model=args.model),
        progress_callback=on_progress,
    )

    if args.json:
        print(json.dumps(asdict(result), indent=2, default=str))

    if result.status == "success" and result.transcript_path:
        print(f"\n{Colors.GREEN}{Colors.BOLD}✓ SUCCESS!{Colors.END}")
        print(f"{Colors.BOLD}Transcript saved to:{Colors.END} {Colors.CYAN}{result.transcript_path}{Colors.END}")
        return 0

    print(f"\n{Colors.RED}{Colors.BOLD}✕ FAILED!{Colors.END}")
    print(f"{Colors.BOLD}Reason:{Colors.END} {result.error}")
    return 1


if __name__ == "__main__":
    # Enable ANSI escape sequences on Windows if needed
    if sys.platform == "win32":
        import os
        os.system("color")
    raise SystemExit(main())

