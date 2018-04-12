# Written by Uriel Kosayev

import pythoncom, pyHook, time

def MK(event):
	return false	
hm = pyHook.HookManager()
hm.MouseAll = MK
hm.KeyAll = MK
hm.HookMouse()
hm.HookKeyboard()
pythoncom.PumpMessages()

# Mouse Lock
def M(event_two):
	return false	
hl = pyHook.HookManager()
hl.MouseAll = M
hl.HookMouse()
pythoncom.PumpMessages()

# Keyboard Lock
def K(event_three):
	return false
hk = pyHook.HookManager()
hk.KeyAll = K
hk.HookKeyboard()
pythoncom.PumpMessages()
