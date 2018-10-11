#!/usr/bin/env python
import pytest
import re
from click.testing import CliRunner

from ..jobcoin import config
from ..jobcoin import cli
from ..jobcoin import jobcoin


@pytest.fixture
def response():
    import requests
    return requests.get('https://jobcoin.gemini.com/')


def test_content(response):
    assert bytes('Hello!', 'utf-8') in response.content


def test_cli_basic():
    targets = ['1234', '4321']
    result = cli.main(targets)
    assert result['exit_code'] == 0
    assert result['mix_addrs']['dst'] == targets


#def test_cli_creates_address():
#    runner = CliRunner()
#    address_create_output = cli.main(['1234', '4321'])


def test_transfer():
    res = jobcoin.transfer('test_address_from', 'test_address_to', 1.0)
    assert res['status'] == 'OK'
    res = jobcoin.transfer('test_address_to', 'test_address_from', 1.0)
    assert res['status'] == 'OK'


def test_transactions():
    res = jobcoin.transactions()
    transactions = [(i.get('fromAddress', None), i['toAddress']) for i in res]
    expected_transactions = [(None, 'Alice'), ('Alice', 'Bob'), (None, 'Casey'), (None, 'Dan'),
            ('Casey', 'Elizabeth'), (None, 'gemini'), (None, 'test_address'),
            (None, 'test_address_from'), ('test_address_from', 'test_address_to'),
            ('test_address_to', 'test_address_from'), (None, 'Frank')]
    for i in expected_transactions:
        assert i in transactions

def test_address_info():
    res = jobcoin.address_info('test_address_from')
    assert float(res['balance']) == 50.0 
