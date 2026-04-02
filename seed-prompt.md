**OPTIMIZED PROMPT**

---

**ROLE:**
You are a senior full-stack systems engineer and developer specializing in cross-platform CLI tools, desktop integrations, and AI-powered audio processing pipelines.

---

**OBJECTIVE:**
Design and implement a **cross-platform audio transcription application** with three interfaces (Right-click OS integration, CLI, and Web UI) that all use a **shared core transcription engine**, powered by **Groq Whisper (large-v3 or turbo)**.

---

## CORE REQUIREMENTS

### 1. Unified Architecture

* Build a modular architecture with:

  * **Core Engine Module** (shared logic)
  * **CLI Interface**
  * **Web Interface (HTTP server, port 3004)**
  * **OS Context Menu Integration (Right-click support)**
* Ensure all interfaces call the same transcription logic (no duplication)

---

### 2. Core Transcription Engine

* Input: audio file path
* Output: `.txt` file in the same directory
* Requirements:

  * Use **Groq API with Whisper large-v3 or turbo**
  * Handle:

    * Different audio formats (mp3, wav, m4a, etc.)
    * Large files (chunking if necessary)
  * Include:

    * Error handling
    * Logging system (file + console)
    * Configurable model selection (large-v3 / turbo)
  * Return structured result (status, transcript path, metadata)

---

### 3. CLI Tool

* Commands:

  * `transcribe <file_path>`
  * Optional flags:

    * `--model`
    * `--output`
    * `--verbose`
* Behavior:

  * Transcribes file
  * Saves `.txt` in same directory (default)
  * Displays progress + completion message

---

### 4. Web Interface (Port 3004)

* Features:

  * Upload or select local file
  * “Start Transcription” button
  * Progress indicator
  * Show result preview
* Backend:

  * REST API endpoint for transcription
* Frontend:

  * Minimal, clean UI (no heavy frameworks required)
* Ensure:

  * Same core engine is reused

---

### 5. Right-Click Integration (Critical Feature)

* When user right-clicks any audio file:
  → Show option: **"Transcribe Audio"**
* On click:

  * Run transcription
  * Generate `.txt` file in same folder

#### Platform Support:

* **Windows**

  * Use registry or shell extension
  * Provide `.reg` or installer script
* **Linux**

  * Use `.desktop` or Nautilus script
* **macOS**

  * Use Automator / Service / Quick Action

---

### 6. Logging & Observability

* Log:

  * File name
  * Timestamp
  * Duration
  * Model used
  * Success / failure
* Store logs in a central location

---

### 7. Extensibility Considerations

* Design for:

  * Future support for batch transcription
  * Multiple output formats (SRT, JSON)
  * Language detection

---

## TECH STACK (RECOMMENDED, BUT FLEXIBLE)

* Backend: Python (preferred) or Node.js
* CLI: argparse / click (Python) or yargs (Node)
* Web: Flask / FastAPI or Express
* OS Integration: Platform-specific scripts
* API: Groq Whisper

---

## OUTPUT FORMAT

Provide:

### 1. Architecture Overview

* Diagram or structured breakdown

### 2. Folder Structure

### 3. Core Engine Implementation (code)

### 4. CLI Implementation (code)

### 5. Web App Implementation (backend + frontend)

### 6. OS Integration Setup

* Windows
* Linux
* macOS

### 7. Setup Instructions

* Installation
* API key setup
* Running each interface

### 8. Future Improvements

---

## CONSTRAINTS

* Code must be clean, modular, and production-ready
* Avoid duplication across interfaces
* Ensure cross-platform compatibility
* Do NOT assume unavailable system permissions
* Handle failures gracefully

---

## ASSUMPTIONS (IF NEEDED)

* User has Groq API key
* Python 3.10+ or Node 18+ available
* Local machine access (not browser-only environment)

---

## QUALITY CHECK

Before finalizing:

* Ensure all three interfaces use the same core logic
* Verify OS integration feasibility
* Confirm API usage correctness
* Validate file handling edge cases

---

**END OF PROMPT**
