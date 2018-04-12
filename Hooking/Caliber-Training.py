# Written by Uriel Kosayev

import pythoncom, pyHook, sys

def caliber(event):
    global i
    if i == 14:
        i = 0
    
    sys.stdout.write(l[i])
    
    i = i + 1
    return False
    
global i
i = 0
l = ['C' ,'a' ,'l' ,'i' ,'b' ,' e' ,'r' ,' -' ,'T' ,'r' ,' a' ,'i' ,'n', 'i', 'n' ,'g\n']

h = pyHook.HookManager()
h.KeyDown = caliber
h.HookKeyboard()
pythoncom.PumpMessages()
