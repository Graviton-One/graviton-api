import pywaves as pw
import requests
import re

default_node = pw.NODE

def restructure_contract_data(contract_address, node_url=default_node):
    data = requests.get(f'{node_url}/addresses/data/{contract_address}').json()
    result = {}
    for i in data:
        test = i.get('key')

        #get id
        x = re.split("(\D+_)+", test)[1:]
        if len(x) > 1 and len(x[1]) > 16:
            x[0] = x[0][:-1:]
            if x[1] not in result:
                result[x[1]] = {}
            else:
                result[x[1]][x[0]] = i.get('value')

    return result

def count_amount(type):
    result = restructure_contract_data('3PEXiW1BrBNMo5A9dfj2CnBW2mwMiaf2sAe')
    # TODO: complete to compute supply consistency

