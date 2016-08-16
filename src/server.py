import socket


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    print('starting')
    conn, addr = server.accept()
    try:
        while True:
            buffer_length = 8
            message_complete = False
            full_string = ""
            while not message_complete:
                part = conn.recv(buffer_length)
                full_string = full_string + part.decode('utf8')
                if len(part) < buffer_length:
                    message_complete = True
            print(full_string)
            conn.sendall(full_string.encode('utf8'))
            server.listen(1)
            conn, addr = server.accept()
    except KeyboardInterrupt:
        conn.close()
        server.close()

server()
