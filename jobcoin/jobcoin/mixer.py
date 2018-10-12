import os
import json
from uuid import uuid4

from . import jobcoin
from . import config


def create_address():
    """
        Create a new empty address by transfering 1 coin into and then back out.
        return value: the uuid of the new address
    """
    uuid = uuid4()
    jobcoin.transfer(config.HOUSE_ADDRESS, uuid.hex, 1.0)
    jobcoin.transfer(uuid.hex, config.HOUSE_ADDRESS, 1.0)
    return uuid.hex


def create_mixer_addresses(branching_factor=5, targets=None, duration=60):
    """
        First create a deposit address, then create a set of target addresses.
        Write the mapping to the database (flat file in this example)
        arguments:
            branching: the number of output addresses that should be generated.
                       ignored if targets are provided
            targets: A list of addresses provided by the user.
            duration: an integer specifying how long to spread the transfers out over
    """

    # Did the user specify some target accounts?
    if targets and isinstance(targets, list):
        dst = targets
    else:
        dst = [create_address() for i in range(branching_factor)]


    addrs = {
        "src": create_address(),
        "dst": dst, 
        "duration": duration,
    }

    # Check the cases for writing the db file
    if os.path.isfile(config.JOBCOIN_DB):
        # The file exist.
        with open(config.JOBCOIN_DB, 'r') as fp:
            try:
                db = json.load(fp)
            except json.decoder.JSONDecodeError:
                print('the database contains corrupt data')
                db = {}

            # Add the new addresses to the db
            if 'mappings' in db:
                db['mappings'].append(addrs)
            else:
                db['mappings'] = [addrs]
    else:
        # The file does not exist
        db = {}

    with open(config.JOBCOIN_DB, 'w') as fp:
        print('Writing db to {}'.format(config.JOBCOIN_DB))
        json.dump(db, fp) 

    return addrs
