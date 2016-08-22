# -*- coding: utf8 -*-
from __future__ import unicode_literals
from server import response_error
from server import response_ok
from server import resolve_uri
from server import parse_request


def server(conn, address):
    """Returns messages to client."""
    try:
        while True:
            conn, addr = server.accept()
            try:
                buffer_length = 8
                message_complete = False
                full_string = b""
                while not message_complete:
                    part = conn.recv(buffer_length)
                    full_string = full_string + part
                    if len(part) < buffer_length:
                        full_string = full_string.decode('utf-8')
                        message_complete = True
                # print('full_string.decode', full_string)
                try:
                    uri = parse_request(full_string)
                    body_tuple = resolve_uri(uri)
                    if body_tuple:
                        response = response_ok(body_tuple)
                    else:
                        response = response_error('404 Not Found')
                    response = response_ok(body)
                except SyntaxError:
                    response = response_error('404 Page Not Found')
                except NameError:
                    response = response_error('405 Method Not Allowed')
                except TypeError:
                    response = response_error('505 HTTP Version Not Supported')
                except ValueError:
                    raise HTTPException(
                        HTTP_BAD_REQUEST,
                        "No 'Host :' in header")
            except SystemError:
                response = response_error()
            conn.sendall(response.encode('utf-8'))
            conn.close()
    except KeyboardInterrupt:
        server.close()


if __name__ == '__main__':
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', 10000), server)
    print('Starting echo server on 1000')
    server.serve_forever()
