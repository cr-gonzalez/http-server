# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import socket
import sys


def client(message):
    """Send a message to the server."""
    message = 'GET /images/Sample_Scene_Balls.jpg HTTP/1.1\r\nHost: '
    info = socket.getaddrinfo('127.0.0.1', 5001)
    stream_info = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    modulo_true = False
    if len(message.encode('utf-8')) % 8 == 0:
        message = message + '\n'
        modulo_true = True
    client.sendall(message.encode('utf8'))
    client.shutdown(socket.SHUT_WR)
    buffer_length = 8
    reply_complete = False
    string = b""
    while not reply_complete:
        part = client.recv(buffer_length)
        string = string + part
        if len(part) < buffer_length:
            print(string.decode('utf8'))
            reply_complete = True
            client.close()
    if modulo_true is True:
        modulo_true is False
        string = string[:-1]
    print(string)
    return string


if __name__ == '__main__':
    message = sys.argv[1]
    client(message)
