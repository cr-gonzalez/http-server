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
            full_string += b"\r\n\r\n" 
            conn.sendall(full_string)
            conn.sendall(response_ok())
            conn.close()
    except KeyboardInterrupt:
        server.close()


def response_ok():
    """Return HTTP 200 OK message for when the connection is ok."""
    return (b"HTTP/1.1 200 OK\r\n\r\n"
            b"Success")


def response_error():
    """Return HTTP 500 Internal Server Error for when problems occur."""
    return (b"HTTP/1.1 500 Internal Server Error\r\n\r\n"
            b"Error, try again later")

if __name__ == '__main__':
    server()
