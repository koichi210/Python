from P4 import P4, P4Exception
from Environment import Environment

p4 = P4()
p4.user = Environment.p4_user
# p4.password = Environment.p4_password
p4.port = Environment.p4_port
p4.client = Environment.p4_client

try:
    # exceptionしてしまう
    p4.run_login()
    opened = p4.run_opened()
except P4Exception:
    for e in p4.errors:
        print(e)
