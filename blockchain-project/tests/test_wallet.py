import unittest
from blockchain.wallet import Wallet

class TestWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()

    def test_wallet_creation(self):
        self.assertIsNotNone(self.wallet.private_key)
        self.assertIsNotNone(self.wallet.public_key)

    def test_sign_transaction(self):
        transaction = {
            'sender': self.wallet.public_key,
            'recipient': 'recipient_address',
            'amount': 10
        }
        signature = self.wallet.sign_transaction(transaction)
        self.assertIsNotNone(signature)

    def test_validate_signature(self):
        transaction = {
            'sender': self.wallet.public_key,
            'recipient': 'recipient_address',
            'amount': 10
        }
        signature = self.wallet.sign_transaction(transaction)
        is_valid = self.wallet.verify_signature(self.wallet.public_key, signature, transaction)
        self.assertTrue(is_valid)

    def test_invalid_signature(self):
        transaction = {
            'sender': self.wallet.public_key,
            'recipient': 'recipient_address',
            'amount': 10
        }
        signature = 'invalid_signature'
        is_valid = self.wallet.verify_signature(self.wallet.public_key, signature, transaction)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()