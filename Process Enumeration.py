import wmi

Proc = wmi.WMI()
Processes = ("List of processes to enumerate")

for process in Proc.Win32_Process():
    if process.Name in Processes:
        print(f"{process.ProcessId} {process.Name}")
