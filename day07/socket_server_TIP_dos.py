'''
TIP服务端
'''
import socket
import os


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
        f = open("vidio.mp4","rb")
        data = f.read()
        conn.sendall(data)
    f.close()
        # print(data.decode())
        # msg = os.popen(data.decode()).read()
        # conn.send(msg.encode("utf-8"))
server.close()
