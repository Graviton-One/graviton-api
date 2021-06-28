from web3 import Web3
from .constants import erc20ABIString

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