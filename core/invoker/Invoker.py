from web3 import Web3
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
ercabipath = os.path.join(THIS_FOLDER, 'abi/erc20.json')

with open(ercabipath) as json_file:
    erc20ABIString = json_file
    
class Invoker:

    def __init__(self, url):
        self.web3 = Web3(Web3.HTTPProvider(url))

    GTON_DECIMALS = 10 ** 18
    erc20ABI = erc20ABIString
    TREASURY_CONTRACT = "0x953555e0Af401Bd031a5a53c72EFa81fae464276"
    GTON_ETHEREUM = "0x01e0E2e61f554eCAaeC0cC933E739Ad90f24a86d"

    def getGtonBalance(self):
        token_contract = self.web3.eth.contract(address=self.GTON_ETHEREUM, abi=self.erc20ABI)
        return token_contract.caller.balanceOf(self.TREASURY_CONTRACT) // self.GTON_DECIMALS