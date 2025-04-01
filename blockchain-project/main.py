from blockchain.blockchain import Blockchain
from api.server import start_server

def main():
    blockchain = Blockchain()
    start_server(blockchain)

if __name__ == "__main__":
    main()