# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import socket
import email.utils
import os
import io


class HTTPException(Exception):
    """Custom exception class."""

    def __init__(self, code, reason):
        self.http_error = code
        self.message = reason


HTTP_BAD_REQUEST = '400 Bad Request'


def server():
    """Start running HTTP server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5001)
    server.bind(address)
    server.listen(1)
    print('starting')
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
            # full_string += b"\r\n\r\n"
            # conn.sendall(full_string)
            conn.sendall(response.encode('utf-8'))
            conn.close()
    except KeyboardInterrupt:
        server.close()


def response_ok(body_tuple):
    """Return 200 ok."""
    first = 'HTTP/1.1 200 OK'
    second_line = 'Content-Type:' + body_tuple[1] + '; charset=utf-8'
    date = 'Date: ' + email.utils.formatdate(usegmt=True)
    header_break = ''
    body = body_tuple
    fourth_line = 'Content-Length: {}'.format(len(body))
    string_list = [first, second_line, date, fourth_line, header_break, body]
    string_list = '\r\n'.join(string_list) + '\r\n'
    string_list = string_list.encode('utf-8') + body
    return string_list


def response_error(error='500 Internal Server Error'):
    """Return 500 internal server error."""
    first = 'HTTP/1.1 {}'.format(error)
    second_line = 'Content-Type: text/plain; charset=utf-8'
    date = email.utils.formatdate(usegmt=True)
    header_break = ''
    body = 'The system is down'
    bytes_ = body.encode('utf-8')
    fourth_line = 'Content-Length: {}'.format(len(bytes_))
    string_list = [first, second_line, date, fourth_line, header_break, body]
    string_list = '\r\n'.join(string_list)
    return string_list


def parse_request(request):
    """Parse GET request from client, return URI."""
    print(request)
    lines = request.split('\r\n\r\n', 1)
    split_lines = lines[0].split('\r\n', 1)
    split_request = split_lines[0].split()
    try:
        method, uri, proto = split_request
        print(proto)
    except ValueError:
        raise SyntaxError
    if not method == 'GET':
        raise NameError
    elif not proto == 'HTTP/1.1':
        print('2', proto)
        raise TypeError
    if 'Host: ' in split_lines[1]:
        return uri
    else:
        raise ValueError


def resolve_uri(uri):
    """Resolve the uri retrned by parse_uri."""
    root = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'webroot')
    full_path = os.path.join(root, uri[1:])
    path_list = uri.split('/')
    path_list = [item for item in path_list if item]
    if path_list == []:
        return html_compiler(full_path)
    file_type = path_list[-1].split('.')
    try:
        if len(file_type) == 1:
            return html_compiler(full_path, uri)
        file = io.open(full_path, 'rb')
        body_content = file.read()
        file_type = file_type[-1]
        return (body_content, file_type)
    except (IOError, OSError):
        return False


def html_compiler(full_path, uri=''):
    """Return a byte encoded html file."""
    file_type = 'text/html'
    list_ = os.listdir(full_path)
    html = '<ul>'
    for file in list_:
        html += '<li><a href="{}/{}">{}</a>/li>'.format(uri, file, file)
        html += '</ul>'
        return (html.encode('utf-8'), file_type)


if __name__ == '__main__':
    server()
