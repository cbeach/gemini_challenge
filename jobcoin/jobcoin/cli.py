#!/usr/bin/env python
import uuid
import sys

from . import mixer, jobcoin


def main(targets=None, branching=1, duration=3600, args=None):
    ret_val = {
        'exit_code': 0,
    }

    ret_val['mix_addrs'] = mixer.create_mixer_addresses(branching, targets=targets)
    return ret_val
