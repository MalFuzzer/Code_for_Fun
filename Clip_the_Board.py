# Written by Uriel Kosayev

import win32clipboard, sys


def grab_data():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def inject_data(data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data)
    win32clipboard.CloseClipboard()


def lock():
    while 1:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText("")
        win32clipboard.CloseClipboard()


option = input('''
Enter your true desires ;): 
1. Inject 
2. Grab
3. Lock
''')

if option not in range(1, 4):
    sys.exit()
else:
    if option == 1:
        data = raw_input("Enter data to set: ")
        inject_data(data)

    elif option == 2:
        print "Here is your desires: {}".format(grab_data())

    elif option == 3:
        lock()
