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
