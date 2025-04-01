class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': self.get_current_timestamp(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def get_current_timestamp(self):
        from time import time
        return time()

    def add_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        import hashlib
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def validate_chain(self):
        for index in range(1, len(self.chain)):
            block = self.chain[index]
            previous_block = self.chain[index - 1]

            if block['previous_hash'] != self.hash(previous_block):
                return False

            if not self.valid_proof(previous_block['proof'], block['proof']):
                return False
        return True

    @staticmethod
    def hash(block):
        import hashlib
        block_string = str(block).encode()
        return hashlib.sha256(block_string).hexdigest()