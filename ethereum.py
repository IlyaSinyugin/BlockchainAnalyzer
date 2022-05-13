from dotenv import load_dotenv
from etherscan import Etherscan
import os

load_dotenv()
# etherscan API from .env 
API = os.getenv("ETHERSCAN_API_KEY")
eth = Etherscan(API)

# Vitalik's address
Wallet_Address = "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"
eth_balance = eth.get_eth_balance(Wallet_Address)
print(float(eth_balance)/1000000000000000000) # dividing since originally it's in wei 

Contract_Address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
eth.get_acc_balance_by_token_and_contract_address(address = Wallet_Address, contract_address = Contract_Address)



#TODO 
# implement the same functionality as in bitcoin.py but for etherscna 