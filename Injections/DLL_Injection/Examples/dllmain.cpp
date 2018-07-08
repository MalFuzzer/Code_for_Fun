// dllmain.cpp : Defines the entry point for the DLL application.

#include "stdafx.h"

#include "dll.h"
#include <windows.h>

#include <stdio.h>
#include <stdlib.h>

DLLEXPORT void mess() {
    MessageBoxA(NULL, "HELLO THERE", "From Notepad", NULL);
}
BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
{
    case DLL_PROCESS_ATTACH: mess(); break;
    case DLL_THREAD_ATTACH: mess(); break;
    case DLL_THREAD_DETACH: mess(); break;
    case DLL_PROCESS_DETACH: mess(); break;
}
return TRUE;
}