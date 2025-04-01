from flask import Flask, jsonify, request
from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction

app = Flask(__name__)
blockchain = Blockchain()

def setup_routes(app: Flask):
    @app.route("/")
    def home():
        return "Welcome to the Blockchain API!"

    @app.route("/blockchain")
    def get_blockchain():
        return {"message": "Blockchain endpoint"}

@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']

    if not all(k in values for k in required):
        return 'Missing values', 400

    transaction = Transaction(values['sender'], values['recipient'], values['amount'])
    blockchain.add_transaction(transaction)

    response = {'message': 'Transaction will be added to the next block'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/mine', methods=['GET'])
def mine():
    blockchain.mine_block()
    response = {
        'message': 'New block mined',
        'index': blockchain.last_block['index'],
        'transactions': blockchain.last_block['transactions'],
        'proof': blockchain.last_block['proof'],
        'previous_hash': blockchain.last_block['previous_hash'],
    }
    return jsonify(response), 200

if __name__ == '__main__':
    setup_routes(app)
    app.run(debug=True)