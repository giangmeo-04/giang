def calculate_hash(block):
    import hashlib
    import json

    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def validate_transaction(transaction):
    if not isinstance(transaction, dict):
        return False
    required_fields = ['sender', 'recipient', 'amount']
    return all(field in transaction for field in required_fields) and transaction['amount'] > 0

def generate_key_pair():
    from Crypto.PublicKey import RSA

    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def sign_transaction(private_key, transaction):
    from Crypto.Signature import pkcs1_15
    from Crypto.Hash import SHA256

    transaction_string = json.dumps(transaction, sort_keys=True).encode()
    transaction_hash = SHA256.new(transaction_string)
    private_key = RSA.import_key(private_key)
    signature = pkcs1_15.new(private_key).sign(transaction_hash)
    return signature

def verify_signature(public_key, transaction, signature):
    from Crypto.Signature import pkcs1_15
    from Crypto.Hash import SHA256

    transaction_string = json.dumps(transaction, sort_keys=True).encode()
    transaction_hash = SHA256.new(transaction_string)
    public_key = RSA.import_key(public_key)
    try:
        pkcs1_15.new(public_key).verify(transaction_hash, signature)
        return True
    except (ValueError, TypeError):
        return False