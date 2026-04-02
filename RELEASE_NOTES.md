# Release Notes

## [v0.0.11] - 2026-04-02

### 🚀 Initial Release - Transcriber Ecosystem

The complete cross-platform, multi-interface transcription engine is now live. This release encompasses the full feature set from core engine to desktop integrations.

#### Key Features:
- **Groq-Powered Whisper Engine**: Sub-second transcription using `whisper-large-v3` and `whisper-large-v3-turbo`. 🧪
- **Infinite Audio Duration**: Automatic `pydub`-based chunking for files exceeding the 25MB Groq API limit. 🧩
- **Modern Web Interface**: Premium "Glassmorphism" UI with real-time job tracking and transcript preview. 🎨
- **OS Native Integrations**: 
  - **Windows**: Right-click "Transcribe Audio" in File Explorer.
  - **Linux**: Nautilus script support.
  - **macOS**: Automator Quick Action integration.
- **Colorful CLI**: Upgraded terminal experience with ANSI status tracking and JSON output support. 🌈
- **Smart Data Safety**: Automatic timestamped copies (e.g., `file_2026.txt`) to prevent overwriting existing transcripts. 🛡️
- **Self-Healing Launchers**: Intelligent `.bat` and `.sh` scripts that auto-rebuild virtual environments and manage `.env` templates. ⚙️

### ⚡ Technical Improvements
- **Structured Resiliency**: All interfaces share a decoupled `TranscriptionEngine` for 100% logic consistency.
- **Configurable Logging**: Unified logging system with the ability to disable persistent logs.
- **Comprehensive Testing**: Full test suite covering core logic, CLI, and Web API lifecycles.

### 📚 Documentation
- Complete `README.md` with visual hero header and detailed quick-start guides.
- In-depth `CODE_DOCUMENTATION.md` explaining the 3-tier architecture.
- `DESIGN_PHILOSOPHY.md` detailing the "Universal Utility" ideology.

---
