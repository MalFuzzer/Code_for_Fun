# Written by Uriel Kosayev

import subprocess as s
import time
import win32gui

prog_name = "Notepad"
my_windows = []
process = s.Popen(["notepad.exe"])
time.sleep(5)

def window_enum(program, window_list):
    header_text = win32gui.GetWindowText(program)
    class_name = win32gui.GetClassName(program)
    if header_text.find(prog_name) >= 0:
        window_list.append((program, header_text, class_name))

win32gui.EnumWindows(window_enum, my_windows)
for program, header_text, class_name in my_windows:
    win32gui.ShowWindow(program, False) # Hide
time.sleep(5)
win32gui.ShowWindow(program, True) # n Seek

process.wait()
print "Done"
