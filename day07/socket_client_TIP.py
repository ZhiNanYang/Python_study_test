'''
TIP客户端
'''

import socket


client = socket.socket()
client.connect(("localhost", 9000))
f = open("text.mp4", "wb")
chang = 0
while True:
    msg = input(">>:").strip()
    if msg == "":
        continue
    client.send(msg.encode())

    data = client.recv(1024)
    chang += len(data)
    print(chang)
    f.write(data)

    # print(data.decode())
f.close()
client.close()
