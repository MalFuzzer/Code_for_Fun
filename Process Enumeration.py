import wmi

Proc = wmi.WMI()
AV_Check = ("List of processes to enumerate")

for process in Proc.Win32_Process():
    if process.Name in AV_Check:
        print(f"{process.ProcessId} {process.Name}")