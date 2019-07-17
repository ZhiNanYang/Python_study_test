'''
TIP服务端
'''
import socket

server = socket.socket()
server.bind(("localhost", 6969))
server.listen(5)
while True:
    print("等待连接")
    conn, addr = server.accept()
    print("连接来了")
    while True:
        try:
            data = conn.recv(1024)
        except ConnectionResetError:
            print("连接断开了")
            break
        print(data.decode())
        conn.send(b"ok,get it")

server.close()
