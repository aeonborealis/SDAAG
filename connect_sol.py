from web3 import Web3

# Connect to a local or remote Solana node
w3 = Web3(Web3.HTTPProvider("https://testnet.solana.com"))

# Verify the connection
if w3.isConnected():
    print("Connected to Solana node")
else:
    print("Not connected to Solana node")
   
# w3 = Web3(Web3.IPCProvider('path/to/solana/ipc'))
# You can also connect to a local Solana node by using 
# the IPC provider instead of the HTTP provider and 
# specifying the path to the IPC file:
