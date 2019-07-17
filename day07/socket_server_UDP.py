'''
UDP服务端
'''

import socket

ip_port = ("127.0.0.1", 9999)
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(ip_port)

while True:
    data, (host, port) = sk.recvfrom(1024)
    print(data.decode(), host, port)
    sk.sendto("ok".encode("utf-8"), (host, port))

