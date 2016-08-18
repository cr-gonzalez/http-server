# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import socket


def server():
    """Start running a server, recieve a clients message, and echo it back."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    print('starting')
    try:
        while True:
            conn, addr = server.accept()
            buffer_length = 8
            message_complete = False
            full_string = b""
            while not message_complete:
                part = conn.recv(buffer_length)
                full_string = full_string + part
                if len(part) < buffer_length:
                    message_complete = True
            print(full_string.decode('utf8'))
            conn.sendall(full_string)
            conn.close()
    except KeyboardInterrupt:
        server.close()

server()
