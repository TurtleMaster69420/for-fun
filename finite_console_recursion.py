# could maybe make better by getting parent command used to run current process and saying "run that" but whatever

import sys
import subprocess
import time

TIME_BUFFER = 0.2
SLEEP_TIME = 4

if len(sys.argv) == 1:
    limit = int(input("Enter number of consoles: "))
else:
    limit = int(sys.argv[1])

print(limit)

if limit:
    time.sleep(TIME_BUFFER)
    subprocess.Popen(f"python {__file__} {limit-1}", creationflags=subprocess.CREATE_NEW_CONSOLE)
    # hydra mode, will create 2**n consoles
    #subprocess.Popen(f"python {__file__} {limit-1}", creationflags=subprocess.CREATE_NEW_CONSOLE)
time.sleep(SLEEP_TIME)
