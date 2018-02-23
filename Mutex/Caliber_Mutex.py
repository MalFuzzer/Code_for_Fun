# Written by Uriel Kosayev

from win32event import CreateMutex
from win32api import GetLastError
from winerror import ERROR_ALREADY_EXISTS
from time import sleep
from sys import exit

handle = CreateMutex(None, 1, 'caliber_mutex')

if GetLastError(  ) == ERROR_ALREADY_EXISTS:
    print 'Process defended by - Caliber_Mutex'
    exit(1)
else:
    for i in range(10):
        print "Don't worry, I have Caliber_mutex to back me up :)", i
        sleep(1)
    print "Thanks for the protection, I'm done"