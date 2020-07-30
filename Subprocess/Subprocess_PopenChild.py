import subprocess

print("Chlid Start")

cmd = "ls -la"
runcmd = subprocess.call(cmd.split())

print("Chlid End")
