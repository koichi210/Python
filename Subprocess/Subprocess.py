import subprocess

#Split渡し
#subprocess.call("ls","-l")

#カンマ区切り渡し
cmd = "ls -l"

print("\n" + "No1 call")
runcmd = subprocess.call(cmd.split())
print(runcmd)

print("\n" + "No2 check_call")
runcmd = subprocess.check_call(cmd.split())
print(runcmd)

print("\n" + "No3 check_output")
runcmd = subprocess.check_output(cmd.split())
print(runcmd)

print("\n" + "No4 Popen")
runcmd = subprocess.check_output(cmd.split())
print(runcmd)
