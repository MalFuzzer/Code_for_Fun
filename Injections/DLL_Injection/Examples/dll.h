#ifndef _DLL_H_
#define _DLL_H_

# define DLLEXPORT __declspec (dllexport)

# define DLLIMPORT __declspec (dllimport)

DLLEXPORT void mess(void);
#endif