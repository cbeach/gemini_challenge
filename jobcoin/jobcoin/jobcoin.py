from . import config

import json
import requests



def transactions():
    return json.loads(requests.get(config.API_TRANSACTIONS_URL).text)


def address_info(address):
    return json.loads(requests.get('{}/{}'.format(config.API_ADDRESS_URL, address)).text)


def transfer(from_address, to_address, amount):
    return json.loads(requests.post(config.API_TRANSACTIONS_URL, 
        data={
            "toAddress": to_address,
            "fromAddress": from_address,
            "amount": amount,
        }).text)

def create(address):
    return json.loads(requests.post(config.API_CREATE_URL, 
        data={
            "address": address,
        }).text)
