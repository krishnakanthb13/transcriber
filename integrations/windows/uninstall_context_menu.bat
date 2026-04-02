@echo off
setlocal

title Uninstall Transcriber Context Menu

set "KEY1=HKCU\Software\Classes\SystemFileAssociations\audio\shell\TranscribeAudio"
set "KEY2=HKCU\Software\Classes\*\shell\TranscribeAudio"

echo ---------------------------------------------------------
echo   Removing "Transcribe Audio" from Context Menu...
echo ---------------------------------------------------------

REM Remove from Location 1
reg query "%KEY1%" >nul 2>nul
if %ERRORLEVEL% equ 0 (
    reg delete "%KEY1%" /f >nul
    echo [INFO] Removed from audio associations.
)

REM Remove from Location 2 (Global Fallback)
reg query "%KEY2%" >nul 2>nul
if %ERRORLEVEL% equ 0 (
    reg delete "%KEY2%" /f >nul
    echo [INFO] Removed from global menu.
)

echo [SUCCESS] "Transcribe Audio" has been removed.
pause
endlocal
