REM --> Written by Uriel Kosayev

@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"

ipconfig > ipconfig.txt
netstat -ano > netstat.txt
tasklist > processes.txt
netstat -rn > routing.txt
netsh advfirewall export "win_firewall.wfw"
net user > users.txt
net group > AD-Groups.txt
net localgroup > localgroup.txt
net localgroup "Administrators" > localgroup_admins.txt
net localgroup "Guests" > localgroup_guests.txt
net localgroup "IIS_IUSRS" > localgroup_IIS.txt
net localgroup "Remote Management Users" > RDP-Users.txt
net share > shares.txt
net session > sessions.txt
REGEDIT /E out.reg
WEVTUtil query-events Security /rd:true /format:text > Security-Events.txt
WEVTUtil query-events System /rd:true /format:text > System-Events.txt
WEVTUtil query-events Application /rd:true /format:text > Application-Events.txt
wmic service get * > services.txt
schtasks > schedule_tasks.txt
dir %appdata%\\Microsoft\\Windows\\"Start Menu"\\Programs\\Startup > startup.txt
dir %programdata%\\Microsoft\\Windows\\"Start Menu"\\Programs\\StartUp > startup_allusers.txt