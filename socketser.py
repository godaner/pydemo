import socket
import time

import tool

port = tool.get_argv_port()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
s.bind((host, port))
s.listen(5)
while 1:
    try:
        cs, addr = s.accept()
        print("连接地址:", addr)
        while 1:
            cs.send("你好".encode('utf-8'))
            time.sleep(1)
    except Exception as e:
        print(e)
