# Analyzing transaction in Bitcoin blockchain 
# Algorithm to output the addresses that the given address has interacted with 

import pandas 

#wallet = str(input("Enter the wallet address: "))
wallet = "bc1q57xhcvleefxz4m2w8ytc6nuy76m4wtjxsw66q6"
transaction_url = 'https://blockchain.info/rawaddr/' + wallet
df = pandas.read_json(transaction_url) # read the json file
transactions=df["txs"]

# saving only the addresses where the given wallet has received crypto from 
# and saving them in a list
addresses_received = []
for i in transactions: 
    for j in i["inputs"]:
        addresses_received.append(i["inputs"][0]["prev_out"]["addr"])

print("Addresses received: ", addresses_received)
with open('transactions.txt', 'w') as f:
    f.write("Addresses received from: " + str(addresses_received)) # writing all received addresses to a file


#df = pandas.DataFrame(transactions(columns=['inputs', 'outputs']))
#df.to_csv('transactions.csv')

# TODO look for another APIs to work with since this one is blocking some amount of transactions
# 
