#!/usr/bin/env python
import pytest
import re
import time

from ..jobcoin import jobcoin
from ..jobcoin import mixer


def test_create_address():
    addr = mixer.create_address()
    res = jobcoin.address_info(addr)

    assert len(res['transactions']) > 0


def test_default_create_mixer_addresses():
    targets = ['1234', '5678']
    addrs = mixer.create_mixer_addresses(targets=targets)
    assert 'src' in addrs
    assert 'dst' in addrs
    assert 'duration' in addrs
    assert addrs['dst'] == targets

#def test_create_mixer_addresses_with_targets():
#    assert len(res['transactions']) > 0

