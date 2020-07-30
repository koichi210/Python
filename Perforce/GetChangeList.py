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

    # NewChangeList
    change = p4.fetch_change()
    change._description = "Hello World\n"
    change._files = file_path
    p4.fetch_change()

    print(change)
    p4_info = p4.run("info")[0] # 情報取得
    workspace_root = p4_info["clientRoot"]
    p4.run_sync()
    p4.run( "change", "-i" )
    # p4.run( "revert", "-a" )
    # p4.run( "client", "-o" )[0]

#    p4.run_submit( change )

    # p4.run("edit", dir_path)
    # p4.run("revert", file_path)
    p4.disconnect()
except P4Exception:
    for e in p4.errors:
        print(e)
