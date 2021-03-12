import pywaves as pw
import requests

default_node = pw.NODE

def get_contract_data(contract_address, node_url=default_node):
    return requests.get(f'{node_url}/addresses/data/{contract_address}').json()
    
def get_data_by_key(contract_address, key, node_url=default_node):
    return requests.get(f'{node_url}/addresses/data/{contract_address}/{key}').json()

def get_contract_data_modified(contract_address, node_url=default_node):
    data = requests.get(f'{node_url}/addresses/data/{contract_address}').json()
    for i in data:
        print(i)
        # test = {'4RCsyYkdHYB8hU5QkLwsuHbkqdVxHQ87xFib4FqLAxy4': { 'type' : 1,  'status' : 2, 'amount' : 10000, 'receiver' : '0x42a938eA05FFA7F65E79610dA9f710EE4C11d020'}}
    return 0