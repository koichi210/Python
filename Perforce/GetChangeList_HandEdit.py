from P4 import P4, P4Exception
from Environment import Environment
import os
import subprocess

def CreateNewChangeList(description):
    try:
        # subout = subprocess.Popen(["dir"], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        # print(subout)
        # for line in iter(subout.stdout.readline,b''):
        #     print(line.rstrip().decode("utf8"))


        # p4in, p4out = os.popen("p4 changelist -i")

#        subout = subprocess.run(["dir"])
#        subout = subprocess.Popen(["dir"])
        p4out = subprocess.Popen(["p4", "changelist -i"], stdout = subprocess.PIPE)
        for e in p4out:
            print(e)

        # p4in, p4out = subprocess.call("p4 changelist -i")
        # p4in.write("change: new\n")
        # p4in.write("description: " + description)
        # p4in.close()
        changelist = p4out.readline().split()[1]
        return changelist
    except P4Exception:
        for e in p4.errors:
            print(e)

def OpenFileForEdit(file, changelist = ""):
    cmd = "p4 edit "
    if changelist:
        cmd += " -c " + changelist + " "
    ret = os.popen(cmd + file).readline().strip()
    if not ret.endswith("opened for edit"):
        print("Couldn't open", file, "for edit:")
        print(ret)

def main():
    p4 = P4()
    p4.user = Environment.p4_user
    # p4.password = Environment.p4_password
    p4.port = Environment.p4_port
    p4.client = Environment.p4_client

    try:
         p4.connect()
        p4_info = p4.run("info")[0]
        # p4.run_login()
    except P4Exception:
        for e in p4.errors:
            print(e)
        return 1

    p4_info = p4.run("info")[0]
    workspace_root = p4_info["clientRoot"]
    image_path = workspace_root + "\\images"
    run_add = False

    dir_path = Environment.target_dir_path
    file_path = Environment.target_file_path

    # ChangeList = CreateNewChangeList("Sample desu")
    print(ChangeList)

if __name__ == '__main__':
    main()
