@echo off

set /P PID=Enter id: 
wmic process get processid, parentprocessid, executablepath | findstr %PID%

set /P PID=Break_point 
