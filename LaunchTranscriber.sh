#!/bin/bash

# Transcriber Launcher - Unix/macOS
APP_NAME="Transcriber"

# Colors for terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}---------------------------------------------------------${NC}"
echo -e "${GREEN}  $APP_NAME Launcher - Powering whisper-large-v3          ${NC}"
echo -e "${GREEN}---------------------------------------------------------${NC}"

# 1. Check for Virtual Environment
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}[INFO] Virtual environment (.venv) not found.${NC}"
    echo -e "${YELLOW}[INFO] Rebuilding project... this may take a minute.${NC}"
    echo
    bash scripts/setup.sh
    if [ $? -ne 0 ]; then
        echo -e "${RED}[ERROR] Setup failed. Please check your internet connection.${NC}"
        exit 1
    fi
fi

# 2. Check for .env file
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}[WARNING] .env file not found.${NC}"
    echo "Creating a template from .env.example..."
    cp .env.example .env
    echo "Please edit .env and set your GROQ_API_KEY."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open -e .env
    else
        nano .env
    fi
    echo "Press Enter when done editing .env..."
    read
fi

# 3. Check for ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo -e "${RED}[ERROR] ffmpeg not found in PATH.${NC}"
    echo "Transcriber requires ffmpeg for audio processing."
    echo "Please install ffmpeg (e.g. 'brew install ffmpeg' or 'sudo apt install ffmpeg')."
    exit 1
fi

# 4. Start the Web App
echo -e "${GREEN}[INFO] Starting Web Server on http://127.0.0.1:3004${NC}"
echo -e "${YELLOW}[INFO] Press Ctrl+C to stop the server.${NC}"

# Trap SIGINT to ensure clean exit
trap "echo -e '\n${RED}[INFO] Shutting down...${NC}'; exit" SIGINT

source .venv/bin/activate
python3 -m transcriber.web.app

if [ $? -ne 0 ]; then
    echo -e "${RED}[ERROR] Web server crashed. Check the logs folder for details.${NC}"
fi
