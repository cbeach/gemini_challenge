#!/usr/bin/env python
import uuid
import sys

from . import mixer, jobcoin


def main(targets=None, branching=1, duration=3600, args=None):
    ret_val = {
        'exit_code': 0,
    }
    print('Welcome to the Jobcoin mixer!\n')
    print('Generating new addresses')
    ret_val['mix_addrs'] = mixer.create_mixer_addresses(branching, targets=targets)
    print('You may now send Jobcoins to address {}'.format(ret_val['mix_addrs']['src']))
    print('They will be mixed and sent to your destination addresses.')
    return ret_val
