# macOS Quick Action Setup

1. Open **Automator** and create a new **Quick Action**.
2. Set:
   - Workflow receives current: `files or folders`
   - In: `Finder`
3. Add **Run Shell Script** action.
4. Configure:
   - Shell: `/bin/bash`
   - Pass input: `as arguments`
5. Script body:

```bash
"/ABSOLUTE/PATH/TO/transcriber/integrations/macos/transcribe-audio-quick-action.sh" "$1"
```

6. Save as `Transcribe Audio`.

To remove later: Finder -> Services Settings -> disable `Transcribe Audio`, or delete the workflow from `~/Library/Services`.
