# Analyzing transaction in Bitcoin blockchain 
# Algorithm to output the addresses that the given address has interacted with 

import pandas 

#wallet = str(input("Enter the wallet address: "))
wallet = "bc1qqpnw6hykw876q49hxcxclhfyy46exjd6ez3046"
transaction_url = 'https://blockchain.info/rawaddr/' + wallet
df = pandas.read_json(transaction_url) # read the json file
transactions=df["txs"]

# saving only the addresses where the given wallet has received crypto from 
# and saving them in a list
addresses_received = []
for i in transactions: 
    inputsList = i["inputs"]
    outputsList = i["out"]
    for j in range(len(inputsList)):
        if inputsList[j]["prev_out"]["addr"] not in addresses_received:
            addresses_received.append(i["inputs"][j]["prev_out"]["addr"])
    for k in range(len(outputsList)):
        if outputsList[k]["addr"] not in addresses_received:
            addresses_received.append(i["out"][k]["addr"])

print("Addresses received: ", addresses_received)
with open('transactions.txt', 'w') as f:
    f.write("Addresses received from: " + str(addresses_received)) # writing all received addresses to a file


#TODO put it in csv
