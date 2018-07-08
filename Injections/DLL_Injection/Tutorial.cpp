// Tutorial.cpp : Defines the entry point for the console application.
//

//We Will Be Using These.
#include "stdafx.h"
#include <windows.h> 
#include <tlhelp32.h> 
#include <shlwapi.h> 
#include <conio.h> 
#include <stdio.h> 

//Lets Just Define Some Variables
#define WIN32_LEAN_AND_MEAN 
#define CREATE_THREAD_ACCESS (PROCESS_CREATE_THREAD | PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION | PROCESS_VM_WRITE | PROCESS_VM_READ


//Lets declare our function
BOOL CreateRemoteThreadInject(DWORD ID, const char * dll);

//Let declare GetProcessId
DWORD GetProcessId(IN PCHAR szExeName);



//Our Application Starts Here.
int main()

{
	//Declare our dll variable
	char dll[10];

	//Get the full path of our .dll
   GetFullPathName("Tutorial.dll",MAX_PATH,dll,NULL); 

 //  Show the .DLL Path.
 //  printf("DLL : ");	
 //  printf(dll);
 //   printf("\n\n\n")

	//We will be using this neat little function written by batfitch - GetProcessId.
	DWORD ID = GetProcessId("notepad.exe");
	if (!CreateRemoteThreadInject(ID,dll))
	{
		//If CreateRemoteThreadInject Returned true
		printf("Injection failed!");
		Sleep(3000);
		exit(1);
		

	}
	else
	{
		//If CreateRemoteThreadInject Returned true
		printf("Injection Successful!");
		Sleep(3000);
		exit(1);
		

	}
     return 0;
}


//Function written by batfitch
DWORD GetProcessId(IN PCHAR szExeName)

{
    DWORD dwRet = 0;
    DWORD dwCount = 0;

    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

    if (hSnapshot != INVALID_HANDLE_VALUE)
    {
        PROCESSENTRY32 pe = {0};
        pe.dwSize = sizeof(PROCESSENTRY32);

        BOOL bRet = Process32First(hSnapshot, &pe);

        while (bRet)
        {
            if (!_stricmp(pe.szExeFile, szExeName))
            {
                dwCount++;
                dwRet = pe.th32ProcessID;
            }
            bRet = Process32Next(hSnapshot, &pe);
        }

        if (dwCount > 1)
            dwRet = 0xFFFFFFFF;

        CloseHandle(hSnapshot);
    }

    return dwRet;
}

//We will be writing our own little function called CreateRemoteThreadInject
BOOL CreateRemoteThreadInject(DWORD ID, const char * dll) 

{ 
//Declare the handle of the process.
   HANDLE Process;

   //Declare the memory we will be allocating
   LPVOID Memory;

   //Declare LoadLibrary
   LPVOID LoadLibrary; 

   //If there's no process ID we return false.
   if(!ID)
	   return false;
     
  //Open the process with read , write and execute priviledges
   Process = OpenProcess(PROCESS_CREATE_THREAD|PROCESS_QUERY_INFORMATION|PROCESS_VM_READ|PROCESS_VM_WRITE|PROCESS_VM_OPERATION, FALSE, ID); 
 
   //Get the address of LoadLibraryA
   LoadLibrary = (LPVOID)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA"); 
 
   // Allocate space in the process for our DLL 
   Memory = (LPVOID)VirtualAllocEx(Process, NULL, strlen(dll), MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE); 
 
   // Write the string name of our DLL in the memory allocated 
   WriteProcessMemory(Process, (LPVOID)Memory, dll, strlen(dll), NULL); 
 
   // Load our DLL 
   CreateRemoteThread(Process, NULL, NULL, (LPTHREAD_START_ROUTINE)LoadLibrary, (LPVOID)Memory, NULL, NULL); 
 
   //Let the program regain control of itself
   CloseHandle(Process);

   VirtualFree((LPVOID)Memory , strlen(dll) , NULL);

   return true;
} 