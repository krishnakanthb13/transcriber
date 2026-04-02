@echo off
setlocal

title Install Transcriber Context Menu

set "SCRIPT_DIR=%~dp0"
set "CLI_BAT=%SCRIPT_DIR%transcribe_cli.bat"

echo ---------------------------------------------------------
echo   Installing "Transcribe Audio" to Context Menu...
echo ---------------------------------------------------------

REM 1. Specific Keys for Audio and All Files
set "KEY1=HKCU\Software\Classes\SystemFileAssociations\audio\shell\TranscribeAudio"
set "KEY2=HKCU\Software\Classes\*\shell\TranscribeAudio"

REM 2. Create the shell keys
reg add "%KEY1%" /v "MUIVerb" /t REG_SZ /d "Transcribe Audio" /f >nul
reg add "%KEY1%" /v "Icon" /t REG_SZ /d "shell32.dll,70" /f >nul
reg add "%KEY1%\command" /ve /t REG_SZ /d "\"%CLI_BAT%\" \"%%1\"" /f >nul

reg add "%KEY2%" /v "MUIVerb" /t REG_SZ /d "Transcribe Audio" /f >nul
reg add "%KEY2%" /v "Icon" /t REG_SZ /d "shell32.dll,70" /f >nul
reg add "%KEY2%\command" /ve /t REG_SZ /d "\"%CLI_BAT%\" \"%%1\"" /f >nul

if %ERRORLEVEL% equ 0 (
    echo [SUCCESS] Installation complete!
    echo.
    echo Testing instructions:
    echo 1. Run "uninstall_context_menu.bat" THEN "install_context_menu.bat" one more time.
    echo 2. Right-click any file and select "Transcribe Audio".
    echo 3. A window SHOULD open with a "[DEBUG]" message.
) else (
    echo [ERROR] Installation failed.
)

pause
endlocal
