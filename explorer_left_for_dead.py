# Written by Uriel Kosayev

import os
import signal
import subprocess as sub
import re
import time

TERM = signal.SIGTERM
PROC  = "explorer.exe\s+(\w+)"
REVIVE = "explorer.exe"

def main():
    while True:
        com = sub.Popen("tasklist", stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        out, err = com.communicate()
        pid = re.findall(PROC, out)
        if pid:
            os.kill(int(pid[0]), TERM)
            #time.sleep(0.2)
	    os.popen1(REVIVE)
	

if __name__ == "__main__":
    main()
