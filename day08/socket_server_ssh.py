import socket
import os

server = socket.socket()
server.bind(("127.0.0.1", 9999))
server.listen(5)
while True:
    print("等待")
    conn, addr = server.accept()
    while True:
        try:
            msg = conn.recv(1024)
        except ConnectionResetError:
            print("断开")
            break
        if not msg:
            print("断开")
            break
        cmd_res = os.popen(msg.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = "指令错误"
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))
        conn.send(cmd_res.encode("utf-8"))
server.close()
