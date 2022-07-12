import socket

import tool

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = tool.get_argv_port()

s.connect((host, port))
while 1:
    try:
        msg = s.recv(1024)
        print(msg.decode("utf-8"))
    except Exception as e:
        print(e)
