# Design Philosophy

## Universal Utility

Transcriber's primary goal is to provide **Instant Accessibility**. Transcription shouldn't require opening a browser, logging into a SaaS, or navigating complex CLI flags. It should be a **single right-click away from your desktop**.

### 1. The "Single Core" Rule
Every interface uses the **exact same code** to process audio.
- This ensures that if the CLI can transcribe an obscure file, the Web UI can too.
- Any improvement to the core logic (better chunking, new models) automatically upgrades every part of the ecosystem.

### 2. Zero Orphan Rule
Our **Launchers (`.bat`/`.sh`)** are designed to be "self-healing".
- They check the environment every single time you launch them.
- If a virtual environment is missing, they rebuild it.
- If an `.env` is missing, they create a template.
- This reduces the "it just opens and closes" frustration for non-technical users.

### 3. Aesthetics: Premium Minimalism
The Web UI follows a **Modern Glassmorphism** design language:
- **Dark Mode by default**: Reduces eye strain and feels more "pro".
- **Dynamic Feedback**: Animated gradient background orbs and real-time progress bars make a slow process (like transcribing 60 minutes) feel much faster.
- **Micro-interactions**: Subtle hover effects on the drag-and-drop zone and status badges clearly communicate which stage the engine is in (validating, transcribing, merging).

### 4. Resilience Over Perfection
The engine is built to **Fail Gracefully**:
- If a single chunk out of ten fails, the engine identifies the error but tries to give you as much of the remaining transcript as possible.
- Files are **never overwritten**. We prioritize data safety over clean folders by adding timestamps to conflicting filenames.

### 5. Local-First Power
While we use a Cloud API (Groq) for the heavy lifting, **the user stays in control**:
- No cloud database is used.
- All files are processed locally and then sent via a secure HTTPS API.
- Your transcripts are saved to **your** machine, in your folders, exactly where you expect them.
