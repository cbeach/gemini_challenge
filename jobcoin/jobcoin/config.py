from pathlib import Path
import sys
import os

# Replace the URL below
API_BASE_URL = "http://jobcoin.gemini.com/greeting/api"
API_ADDRESS_URL = '{}/addresses'.format(API_BASE_URL)
API_CREATE_URL = 'https://jobcoin.gemini.com/greeting/create'
API_TRANSACTIONS_URL = '{}/transactions'.format(API_BASE_URL)
HOUSE_ADDRESS = 'gemini'

HOME_DIR = Path.home()
JOBCOIN_DB = os.path.join(HOME_DIR, '.jobcoin.db.json')
