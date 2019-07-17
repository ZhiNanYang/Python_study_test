import socket
import hashlib

client = socket.socket()
client.connect(("localhost", 9999))

while True:

    cmd = input(">>:").strip()
    if cmd == "":
        continue
    elif cmd.startswith("get"):
        client.send(cmd.encode())
        file_size = int(client.recv(1024).decode())
        f = open(cmd.split()[1] + ".new", "wb")
        recv_size = 0
        m = hashlib.md5()
        client.send("开始接受数据".encode())
        while recv_size < file_size:
            surplus = file_size - recv_size
            if surplus > 1024:
                size = 1024
            else:
                size = surplus
            data = client.recv(size)
            recv_size += len(data)
            m.update(data)
            f.write(data)
        else:
            f.close()
            print("file md5:", client.recv(1024).decode())
            print("recv file md5:", m.hexdigest())
    else:
        continue
