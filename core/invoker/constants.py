import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
ercabipath = os.path.join(THIS_FOLDER, 'abi/erc20.json')

with open(ercabipath) as json_file:
    erc20ABIString = json_file.read()

INFURA_URL = "https://mainnet.infura.io/v3/d456e06a80f44aca9e273f0172d035f1"