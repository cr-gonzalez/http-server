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


def test_response_ok():
    """Check that response_ok returns '200 OK'."""
    from server import response_ok
    assert response_ok().split(b'\r\n\r\n')[0] == b'HTTP/1.1 200 OK'


def test_response_error():
    """Test that response_error returns '500 Internal Server Error'."""
    from server import response_error
    error_text = b'HTTP/1.1 500 Internal Server Error'
    assert response_error().split(b'\r\n\r\n')[0] == error_text
