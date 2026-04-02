@echo off
setlocal

title Transcriber CLI

set "SCRIPT_DIR=%~dp0"
set "REPO_ROOT=%SCRIPT_DIR%..\..\"
pushd "%REPO_ROOT%" >nul
set "REPO_ROOT_ABS=%CD%"
popd >nul

set "EXE_PATH=%REPO_ROOT_ABS%\.venv\Scripts\transcribe.exe"

REM Check if virtual env is ready
if not exist "%EXE_PATH%" goto :no_venv

REM Call the transcriber CLI with all provided arguments
echo [INFO] Running transcription...
"%EXE_PATH%" %*

if %ERRORLEVEL% neq 0 goto :failed

echo [SUCCESS] Transcription finished.
pause
goto :end

:no_venv
echo [ERROR] Virtual environment not found at: %EXE_PATH%
echo Please run the setup script first.
pause
exit /b 1

:failed
echo [ERROR] Transcription failed with exit code %ERRORLEVEL%.
pause
exit /b %ERRORLEVEL%

:end
endlocal
