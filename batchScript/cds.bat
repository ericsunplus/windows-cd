@echo off
SET argument=%*

FOR /F "tokens=* USEBACKQ" %%F IN (`python %pythondir%\cds.py %argument%`) DO (
    if not exist "%%F\*" echo %%F
    SET possibleDir=%%F
)

:: If a valid dir is returned, switch to it
if defined possibleDir (
    if exist "%possibleDir%\*" call cd /d "%possibleDir%"
)
