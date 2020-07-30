import os
import subprocess
 
print("Main Start")
 
cmd = "Python " + os.getcwd() + "\Subprocess_PopenChild.py"
#cmd = "Python Subprocess_PopenChild.py"
subprocess.Popen(cmd.split())

print("Main End")
