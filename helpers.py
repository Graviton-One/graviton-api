import pywaves as pw
import requests

default_node = pw.NODE

def get_contract_data(contract_address, node_url=default_node):
    return requests.get(f'{node_url}/addresses/data/{contract_address}').json()
    
def get_data_by_key(contract_address, key, node_url=default_node):
    return requests.get(f'{node_url}/addresses/data/{contract_address}/{key}').json()