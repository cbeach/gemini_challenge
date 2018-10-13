import json
from jobcoin import mixer, jobcoin, config

with open(config.JOBCOIN_DB, 'r') as fp:
    addrs_to_check = json.load(fp)['mappings']

for i in addrs_to_check:
    src_info = jobcoin.address_info(i['src'])
    src_balance = float(src_info['balance'])

    print('src: {} - {}'.format(i['src'], src_balance))
    print('==============================')
    dst_balances = []
    for j in i['dst']:
        info = jobcoin.address_info(j)
        balance = float(info['balance'])
        dst_balances.append(balance)
        print('    {}: {}'.format(j, balance))
    print('sum(dst): {}'.format(sum(dst_balances)))
    print('==============================\n')
