#include <Windows.h>
#include <iostream>
#include <string>
#include <vector>

// Reads process memory by given PID
char* GetAddressOfData(DWORD pid, const char *data, size_t len)
{
    HANDLE process = OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, FALSE, pid);
    if(process)
    {
        SYSTEM_INFO si;
        GetSystemInfo(&si);

        MEMORY_BASIC_INFORMATION info;
        std::vector<char> chunk;
        char* p = 0;
        while(p < si.lpMaximumApplicationAddress)
        {
            if(VirtualQueryEx(process, p, &info, sizeof(info)) == sizeof(info))
            {
                p = (char*)info.BaseAddress;
                chunk.resize(info.RegionSize);
                SIZE_T bytesRead;
                if(ReadProcessMemory(process, p, &chunk[0], info.RegionSize, &bytesRead))
                {
                    for(size_t i = 0; i < (bytesRead - len); ++i)
                    {
                        if(memcmp(data, &chunk[i], len) == 0)
                        {
                            return (char*)p + i;
                        }
                    }
                }
                p += info.RegionSize;
            }
        }
    }
    return 0;
}

// Terminate process function
BOOL TerminateProcessEx(DWORD dwProcessId, UINT uExitCode)
{
    DWORD dwDesiredAccess = PROCESS_TERMINATE;
    BOOL  bInheritHandle  = FALSE;
    HANDLE hProcess = OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId);
    if (hProcess == NULL)
        return FALSE;

    BOOL result = TerminateProcess(hProcess, uExitCode);

    CloseHandle(hProcess);

    return result;
}

// Main
int main()
{
    const char someData[] = "malware";
    DWORD pid;
    for(pid = 11340; pid <= 11350; pid++) // Range of pids to scan
    {
        char* ret = GetAddressOfData(pid, someData, sizeof(someData));
        if(ret)
        {
            std::cout << "Malware Alert!!! at: " << (void*)ret << "\n";
            TerminateProcessEx(pid, 0);
            continue;
        }
    }
    return 0;
}