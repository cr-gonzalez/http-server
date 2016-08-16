# -*- coding:utf-8 -*-

import socket
import sys


def client(message):
    info = socket.getaddrinfo('127.0.0.1', 5000)
    print(info)
    stream_info = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    print(stream_info)
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf8'))
    buffer_length = 40
    reply_complete = False
    string = ""
    while not reply_complete:
        part = client.recv(buffer_length)
        string = string + part.decode('utf8')
        if len(part) < buffer_length:
            reply_complete is True
            client.close()


if __name__ == '__main__':
    message = sys.argv[1]
    client(message)
