import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
ercabipath = os.path.join(THIS_FOLDER, 'abi/erc20.json')

with open(ercabipath) as json_file:
    erc20ABIString = json_file.read()

INFURA_URL = "https://mainnet.infura.io/v3/ec6afadb1810471dbb600f24b86391d2"