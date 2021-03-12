import requests
bscscan_public_api_url = 'https://api.bscscan.com/api'

def get_token_supply_data(contract_address, api_url=bscscan_public_api_url):
    return int(requests.get(f'{api_url}?module=stats&action=tokensupply&contractaddress={contract_address}').json()['result'])/10**18


