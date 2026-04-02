# Social Media Announcements

## [v0.0.11] - 2026-04-02

### 🌐 LinkedIn Post
---
**Style**: Professional, exciting tone focusing on "value add".
**Format**: Plain text only.

Transcriber v0.0.11: The Ultimate Cross-Platform Audio Transcription Engine is Live! 🚀

Tired of context-switching between different tools just to transcribe audio? 
Today, we’re launching the Transcribing ecosystem: a unified suite of tools designed for instant, high-speed audio transcription with zero overhead.

Built on the lightning-fast Groq Cloud Whisper API, Transcriber offers:

1. 🖱️ OS Integration: Right-click transcribe any file directly from Windows File Explorer, macOS Finder, or Linux Nautilus.
2. 🧩 Large File Support: Our "infinite audio" engine automatically chunks files that exceed standard API limits—no more manual splitting!
3. 🎨 Modern Web Interface: A premium, dark-themed "glassmorphism" UI with drag-and-drop and real-time job tracking.
4. 🌈 Colorful CLI: A specialized tool for power users with JSON output support and structured logging.

Everything is local-first, privacy-conscious, and powered by our "Zero Orphan" self-healing launchers.

Check out the repository here: https://github.com/krishnakanthb13/transcriber

#OpenSource #AudioTranscription #GroqCloud #WhisperAPI #FastAPI #Productivity

---

### 🛡️ Reddit Post
---
**Style**: Extensive, conversational "Show don't tell". 
**Format**: Markdown supported.
**Suggested Subreddits**: r/programming, r/webdev, r/opensource, r/Python

**Suggested Title**: I built a cross-platform transcription ecosystem with 'infinite' duration support using Groq Whisper.

**Content**:

Hey everyone! 🌟

I wanted to share a project I've been working on to solve a personal pain point: transcribing long audio files quickly and without context-switching.

**Transcriber** is a unified transcription tool that gives you three different ways to handle your audio—all sharing a single, robust core engine:

1.  **OS Native Right-Click**: You can transcribe directly from your file explorer. I've implemented registry-based context menus for Windows, Nautilus scripts for Linux, and Automator Quick Actions for macOS.
2.  **Modern Web UI**: A FastAPI-powered app with a "glassmorphism" aesthetic. It handles background jobs asynchronously, so you don't have to stay on the page.
3.  **CLI**: For those who live in the terminal, the `transcribe` command is colorful, supports JSON outputs, and integrates with any script.

**The "Infinite" Duration Challenge:**
Groq's API has a 25MB limit. To solve this, I built a `ChunkPlanner` that automatically splits files into manageable segments using `pydub`, processes them sequentially, and merges the text back into a single, timestamp-safe `.txt` file.

**Key Tech Stack:**
-   **Backend**: Python, FastAPI, Uvicorn
-   **AI**: Groq Whisper API (whisper-large-v3)
-   **Processing**: Pydub, FFmpeg
-   **UI**: Glassmorphism HTML/CSS

Check out the source code and documentation below:
https://github.com/krishnakanthb13/transcriber

I'd love to hear your thoughts on the OS-integration approach!

---

### 🐦 X (Twitter) Post
---
**Style**: Crisp, punchy, crisp content.
**Format**: Plain text only.

Transcriber v0.0.11 is here! 🚀

Native right-click transcription for Windows, Linux, and macOS.
Infinite duration audio support via automatic chunking.
Premium Glassmorphism Web UI + Colorful CLI.

Powered by Groq Whisper for insane speed.

Try it now: https://github.com/krishnakanthb13/transcriber 

#Transcription #OpenSource #Groq #Python
---
