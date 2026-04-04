# Contributing to Transcriber

First off, thank you for considering contributing to Transcriber! It's people like you that make it such a great tool.

## Bug Reporting

If you encounter a bug, please create an issue on GitHub with the following information:
- **Environment**: OS (Windows/Linux/macOS), Python version.
- **Reproducible Steps**: Step-by-step actions that lead to the bug.
- **Expected vs Actual Behavior**: What you expected to happen vs what actually happened.
- **Logs**: If applicable, attach the output from `logs/transcriber.log` or the CLI output.

## Feature Suggestions

We love new ideas! If you have a feature request:
- Open a new issue with the `enhancement` label.
- Provide a **Problem Definition**: What problem does this solve?
- Provide an **Expected Solution**: How would the ideal feature look or act?
- Be mindful of the **Design Philosophy** (minimalism, local-first power, single core rule).

## Standard Workflow

1. **Fork** the repository.
2. **Branch** off from `main` (`git checkout -b feature/your-feature-name`).
3. **Commit** your changes (`git commit -m 'Add new feature'`).
4. **Push** your branch (`git push origin feature/your-feature-name`).
5. **Create a Pull Request** via GitHub.

## Local Development Setup

To get your development environment running locally:

```bash
# 1. Clone your fork
git clone https://github.com/your-username/transcriber.git
cd transcriber

# 2. Run the setup scripts (creates virtual env)
# Windows
.\scripts\setup.ps1
# Linux/macOS
bash scripts/setup.sh

# 3. Activate virtual environment
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

# 4. Install Dev Dependencies
pip install -e ".[dev]"
```

## Pre-Submission Checklist

Before submitting your PR, ensure the following pass:

- [ ] **Tests**: Run `pytest` to ensure all core behaviors pass.
- [ ] **Code Quality**: Ensure variables and logic adhere to the existing structure.
- [ ] **Documentation**: If adding a feature, update `CODE_DOCUMENTATION.md` or `README.md` if necessary.
- [ ] **Data Safety**: Ensure you don't override the `Timestamped file renaming` protection.
