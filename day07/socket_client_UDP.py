'''
UDP客户端
'''

import socket

ip_port = ("127.0.0.1", 9999)
sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
    inp = input("数据：").strip()
    if inp == "exit":
        break
    sk.sendto(inp.encode("utf-8"), ip_port)
    data = sk.recvfrom(1024)
    print(data)

sk.close()
