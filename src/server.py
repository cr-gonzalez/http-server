import socket


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    print(server)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    print(server)
    server.listen(1)
    print('starting')
    info = socket.getaddrinfo('127.0.0.1', 5000)
    print(info)
    conn, addr = server.accept()
    buffer_length = 40
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            message_complete is True
            message = "string"
            conn.sendall(message.encode('utf8'))
            conn.close()
            server.close()


server()
