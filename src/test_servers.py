# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import pytest


MESSAGE_TABLE = [
    ('TEST', 'TEST'),
    ('TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST',
     'TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST'),
    ('TESTTEST', 'TESTTEST'),
    ('TESTÖ☻ê£', 'TESTÖ☻ê£')
]



@pytest.fixture(scope="function")
def response_ok():
    """Return 200 ok."""
    first = u'HTTP/1.1 200 OK'
    second_line = u'Content-Type: text/plain; charset=utf-8'
    header_break = u''
    body = u'/'
    bytes_ = body.encode('utf-8')
    fourth_line = u'Content-Length: {}'.format(len(bytes_))
    string_list = [first, second_line, fourth_line, header_break, body]
    string_list = '\r\n'.join(string_list)
    return string_list


@pytest.mark.parametrize('value, result', MESSAGE_TABLE)
def test_client(value, result):
    """Test client."""
    from client import client
    client(value)
    assert value == result


# def test_response_ok(response_ok):
#     """Test that response_ok returns '200 OK'"""
#     uri = '/filepath'
#     """Check that response_ok returns '200 OK'."""
#     from server import response_ok
#     assert response_ok(uri).split(b'\r\n\r\n')[0] == b'HTTP/1.1 /filepath 200 OK'


# def test_response_error():
#     """Test that response_error returns '500 Internal Server Error'."""
#     from server import response_error
#     error_text = b'HTTP/1.1 500 Internal Server Error'
#     assert response_error().split(b'\r\n\r\n')[0] == error_text


def test_parse_request():
    """."""
    from server import parse_request
    assert parse_request('GET /filepath HTTP/1.1\r\nHost: ') == '/filepath'


def test_parse_nameerror():
    """."""
    from server import parse_request
    with pytest.raises(NameError):
        parse_request('PUT / HTTP/1.1')


def test_parse_typeerror():
    """."""
    from server import parse_request
    with pytest.raises(TypeError):
        parse_request('GET / HTTP/2.1')


def test_parse_syntaxerror():
    """."""
    from server import parse_request
    with pytest.raises(SyntaxError):
        parse_request('GET  HTTP/1.1')


def test_resolve_uri_nonexistant_file():
    """Assert function returns the correct body."""
    from server import resolve_uri
    path = resolve_uri('/WTF.txt')
    result = False
    assert path == result


def test_resolve_uri_nonexistant_dir():
    """Assert function returns the correct body."""
    from server import resolve_uri
    path = resolve_uri('/WTF')
    result = False
    assert path == result


def test_resolve_uri_images():
    """Test image files are present."""
    from server import resolve_uri
    our_tuple = resolve_uri('/images/Sample_Scene_Balls.jpg')
    assert our_tuple[1] == 'jpg'


def test_resolve_uri_files():
    """Test image files are present."""
    from server import resolve_uri
    our_tuple = resolve_uri('/sample.txt')
    assert our_tuple[1] == 'txt'


def test_resolve_uri_dir():
    """Test image files are present."""
    from server import resolve_uri
    our_tuple = resolve_uri('/images')
    assert our_tuple[1] == 'text/html'
