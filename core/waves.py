import pywaves as pw
import requests
import re

default_node = pw.NODE

def get_contract_data(contract_address, node_url=default_node):
    return requests.get(f'{node_url}/addresses/data/{contract_address}').json()
    
def get_data_by_key(contract_address, key, node_url=default_node):
    return requests.get(f'{node_url}/addresses/data/{contract_address}/{key}').json()

def restructure_contract_data(contract_address, node_url=default_node):
    data = requests.get(f'{node_url}/addresses/data/{contract_address}').json()
    result = {}

    for kv in data:
        x = re.split("(\D+_)+", kv.get('key'))[1:]

        if len(x) > 1 and len(x[1]) > 16:
            x[0] = x[0][:-1:] # stripping the last underscore from key
            
            if x[1] not in result:
                result[x[1]] = {}
                result[x[1]][x[0]] = kv.get('value')
            else:
                result[x[1]][x[0]] = kv.get('value')

    return result

def count_usdn_locked_amount(contract_address): # TODO check consistency
    result = restructure_contract_data(contract_address)
    amount = float(0)
    for kv in result:
        if result[kv].get('rq_status') == 1 and result[kv].get('rq_type') == 1: 
            amount += result[kv].get('rq_amount')
    return amount/10**6



