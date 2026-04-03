# Social Media Announcements

## [v0.0.17] - 2026-04-03

### 🌐 LinkedIn Post
---
**Style**: Professional, exciting tone focusing on "value add".
**Format**: Plain text only.

Transcriber v0.0.17: Smarter, Faster, and more Persistent! 🚀 

We’ve just shipped a major update to Transcriber, our cross-platform transcription ecosystem. This release focuses on developer experience, user workflow, and smarter transcription logic.

New in v0.0.17:
1. 🔄 History Panel & Persistence: No more losing your past transcriptions! With local-first persistence, your history is saved right in your browser.
2. 🧩 Context-Aware Chunking: We’ve moved beyond simple sequential splits. Our new overlapping chunking strategy ensures that context is preserved across audio segments, making transcriptions for technical jargon much more accurate.
3. 🔁 Self-Healing Pipeline: Enhanced retry logic means transient API hiccups won't break your long-duration transcription jobs.
4. 📜 Open Source Governance: We’ve officially adopted the GNU GPL v3 license and launched our first contributing guide!

Experience the new web interface and improved core engine today.

Repositiory: https://github.com/krishnakanthb13/transcriber

#OpenSource #AudioTranscription #Transcription #Python #FastAPI #WebDev #ProductivityTools

---

### 🛡️ Reddit Post
---
**Style**: Extensive, conversational "Show don't tell". 
**Format**: Markdown supported.
**Suggested Subreddits**: r/programming, r/webdev, r/opensource, r/Python

**Suggested Title**: I added overlapping chunking and local-first history to my cross-platform transcriber!

**Content**:

Hey everyone! 🌟

I’ve been hard at work on **Transcriber**, and today I’m excited to share the v0.0.17 update!

The biggest challenge with long audio transcription (beyond the 25MB Groq API limit) was preserving context at the split points. Traditional sequential chunking sometimes cut off mid-jargon, leading to weird transcription errors. 

**What's New in v0.0.17:**

1.  **Overlapping Chunking**: The engine now overlaps segments by a few seconds. This preserves local context, which is then reconciled during the merge phase for much higher accuracy.
2.  **Local-First History**: I added a history panel to the web UI. It uses `localStorage` for zero-setup persistence—your history stays on your machine, no database required.
3.  **Pipeline Resiliency**: Added automatic retries for the transcription pipeline. If an API call fails mid-way through an hour-long file, it now gracefully recovers.
4.  **Open Source Growth**: Officially moved to GNU GPL v3 and added a `CONTRIBUTING.md` to help others get involved.

**Key Tech Updates:**
-   **Core**: Improved `ChunkPlanner` with context-overlap logic.
-   **UI**: Enhanced glassmorphism sidebar for history management.
-   **Legal**: GPL v3 license integrated.

Check out the update here:
https://github.com/krishnakanthb13/transcriber

I’d love to hear how you guys handle context reconciliation in your AI pipelines!

---

### 🐦 X (Twitter) Post
---
**Style**: Crisp, punchy, crisp content.
**Format**: Plain text only.

Transcriber v0.0.17 is out! 🚀

🔄 Local-first History Panel in Web UI.
🧩 Smart Overlapping Chunking for better context.
🔁 Automated Retry Logic for resilient pipelines.
📜 Now officially under GNU GPL v3!

Smarter transcripts, same insane speed. ⚡

Try it: https://github.com/krishnakanthb13/transcriber

#Transcription #OpenSource #Groq #Python #AI

---

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
