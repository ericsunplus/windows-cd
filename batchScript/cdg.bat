@echo off
python %pythondir%\cdg.py %* > %userprofile%\__tempcd.bat
call %userprofile%\__tempcd.bat
del %userprofile%\__tempcd.bat
