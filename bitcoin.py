# Analyzing transaction in Bitcoin blockchain 
# Algorithm to output the addresses that the given address has interacted with 

import pandas 

wallet = str(input("Enter the wallet address: "))
transaction_url = 'https://blockchain.info/rawaddr/' + wallet
df = pandas.read_json(transaction_url)
transactions=df["txs"]
print(transactions)