@echo off

echo "List History:"
echo.

reg query HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU

echo "Wired interfaces:"
echo.
netsh lan show interfaces
echo "Wireless-LAN interfaces:"
echo.
netsh wlan show interfaces

set /P INPUT=BREAKPOINT