# Blockchain Project

This project is a simple implementation of a blockchain using Python. It includes features for creating transactions, managing a blockchain, and setting up a network of nodes.

## Features

- **Blockchain**: A class that manages the chain of blocks, handles adding new blocks, and validates the blockchain.
- **Blocks**: Each block contains an index, timestamp, transactions, previous hash, and methods for calculating its hash.
- **Transactions**: A class that represents a transaction with sender, recipient, and amount properties.
- **Wallet**: Manages user wallets, including key generation and transaction signing.
- **Network**: Nodes that communicate with each other to maintain a distributed ledger.
- **API**: A Flask-based API for interacting with the blockchain, including endpoints for creating transactions and retrieving the blockchain.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd blockchain-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python main.py
```

This will start the Flask server and initialize the blockchain.

## Testing

To run the tests, use:
```
pytest
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.