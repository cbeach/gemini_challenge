#!/usr/bin/env python
import pytest
import re
from click.testing import CliRunner

from ..jobcoin import config
from ..jobcoin import jobcoin
from .. import cli


@pytest.fixture
def response():
    import requests
    return requests.get('https://jobcoin.gemini.com/')


def test_content(response):
    assert bytes('Hello!', 'utf-8') in response.content


def test_cli_basic():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'Welcome to the Jobcoin mixer' in result.output


def test_cli_creates_address():
    runner = CliRunner()
    address_create_output = runner.invoke(cli.main, input='1234,4321').output
    output_re = re.compile(
        r'You may now send Jobcoins to address [0-9a-zA-Z]{32}. '
        'They will be mixed and sent to your destination addresses.'
    )
    assert output_re.search(address_create_output) is not None


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
