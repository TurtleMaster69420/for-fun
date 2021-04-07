import sys
import time
import os
import subprocess
if len(sys.argv) == 1:
    print("Enter limit: ")
    limit = int(input())
    file_id = 1
else:
    limit = int(sys.argv[2])
    if limit == 0:
        time.sleep(4)
        quit()
    file_id = int(sys.argv[1])
    print(file_id)  

with open(f"finite_file_recursion{file_id}.py") as f:
    with open(f"finite_file_recursion{file_id + 1}.py", "w") as g:
        g.write(f.read())


print("spam")
subprocess.run(f"python finite_file_recursion{file_id}.py {file_id + 1} {limit-1}", creationflags=subprocess.CREATE_NEW_CONSOLE)
