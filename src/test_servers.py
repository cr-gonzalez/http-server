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


@pytest.mark.parametrize('value, result', MESSAGE_TABLE)
def test_client(value, result):
    """Test client."""
    from client import client
    client(value)
    assert value == result


def test_response_ok(uri):
    """Test that response_ok returns '200 OK'"""
    uri = '/filepath'
    """Check that response_ok returns '200 OK'."""
    from server import response_ok
    assert response_ok(uri).split(b'\r\n\r\n')[0] == b'HTTP/1.1 /filepath 200 OK'


def test_response_error():
    """Test that response_error returns '500 Internal Server Error'."""
    from server import response_error
    error_text = b'HTTP/1.1 500 Internal Server Error'
    assert response_error().split(b'\r\n\r\n')[0] == error_text


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
