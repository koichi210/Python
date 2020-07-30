from P4 import P4, P4Exception
from Environment import Environment

p4 = P4()
p4.user = Environment.p4_user
# p4.password = Environment.p4_password
p4.port = Environment.p4_port
p4.client = Environment.p4_client

dir_path = Environment.target_dir_path
file_path = Environment.target_file_path

try:
    p4.connect()
    p4.run("edit", dir_path)
    p4.run("revert", file_path)
    p4.disconnect()
except P4Exception:
    for e in p4.errors:
        print(e)
