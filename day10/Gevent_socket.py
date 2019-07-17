#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 12:51:02
# @Author  : Your Name (you@example.org)

import sys
import socket
import time
import gevent

from gevent import socket, monkey
monkey.patch_all()


def server(port):
    s = socket.socket()
    s.bind(('localhost', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)


def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
                print("shutdown")

    except Exception as ex:
        print(ex)
    finally:
        conn.close()


if __name__ == '__main__':
    server(8001)
