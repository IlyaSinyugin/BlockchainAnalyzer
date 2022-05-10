from dotenv import load_dotenv
import os

load_dotenv()
# etherscan API from .env 
API = os.getenv("ETHERSCAN_API_KEY")

print(API)

#TODO 
# implement the same functionality as in bitcoin.py but for etherscna 