import socket
import os
import hashlib


server = socket.socket()
server.bind(("localhost", 9999))
server.listen(5)

while True:
    print("等待客户")
    conn, addr = server.accept()
    print(str(addr), "接入")
    while True:
        try:
            cmd = conn.recv(1024)
            filename = cmd.split()[1]
            if os.path.isfile(filename):
                file_size = os.stat(filename).st_size
                conn.send(str(file_size).encode())
                conn.recv(1024)
                f = open(filename, "rb")
                m = hashlib.md5()
                for line in f:
                    m.update(line)
                    conn.send(line)
                else:
                    f.close()
                    conn.send(m.hexdigest().encode())
                    print("文件传输完成。")
        except (ConnectionResetError, ConnectionAbortedError):
            print(str(addr), "断开连接")
            break
    conn.close()
