#include <Windows.h>
#include <iostream>
#include <vector>
#include <Tlhelp32.h>

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

std::vector<DWORD> EnumProcs()
{
    std::vector<DWORD> pids;
    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (snapshot != INVALID_HANDLE_VALUE)
    {
        PROCESSENTRY32 pe32 = { sizeof(PROCESSENTRY32) };
        if (Process32First(snapshot, &pe32))
        {
            do
            {
                pids.push_back(pe32.th32ProcessID);
            } while (Process32Next(snapshot, &pe32));
        }
        CloseHandle(snapshot);
    }
    return pids;
}

int main()
{
    const char someData[] = "malware";
    std::vector<DWORD> pids = EnumProcs();

    for (size_t i = 0; i < pids.size(); i++)
    {
        char* ret = GetAddressOfData(pids[i], someData, sizeof(someData));
        if(ret)
        {
            std::cout << "Malware Alert!!! at: " << (void*)ret << "\n";
            TerminateProcessEx(pids[i], 0);
            continue;
        } 
    }
    return 0;
}
