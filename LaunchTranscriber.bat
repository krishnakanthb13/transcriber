@echo off
setlocal

title Transcriber Web Interface

echo ---------------------------------------------------------
echo   Transcriber Launcher - Powering whisper-large-v3
echo ---------------------------------------------------------

rem 1. Check for Virtual Environment
if not exist ".venv" goto :novenv

rem 2. Check for .env file
if not exist ".env" goto :noenv

:checkffmpeg
rem 3. Check for ffmpeg
echo [INFO] Checking for ffmpeg...
where ffmpeg >nul 2>nul
if %ERRORLEVEL% neq 0 goto :noffmpeg

rem 4. Start the Web App
echo [INFO] Starting Web Server on http://127.0.0.1:3004
echo [INFO] Press Ctrl+C to stop the server.

.\.venv\Scripts\python.exe -m transcriber.web.app

if %ERRORLEVEL% neq 0 goto :crash
goto :end

:novenv
echo [INFO] Virtual environment (.venv) not found.
echo [INFO] Rebuilding project... this may take a minute.
echo.
powershell.exe -ExecutionPolicy Bypass -File scripts\setup.ps1
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Setup failed. Please check your internet connection.
    pause
    exit /b 1
)
goto :checkffmpeg

:noenv
echo [WARNING] .env file not found. 
echo [INFO] Creating a template from .env.example...
copy .env.example .env >nul
echo [INFO] Opening .env for you to set GROQ_API_KEY.
notepad .env
echo.
echo Please save the .env file and press any key to continue...
pause >nul
goto :checkffmpeg

:noffmpeg
echo [ERROR] ffmpeg not found in PATH.
echo Transcriber requires ffmpeg for audio processing.
echo Please install ffmpeg and add it to your PATH.
pause
exit /b 1

:crash
echo [ERROR] Web server crashed or was stopped with an error.
pause
exit /b 1

:end
endlocal
