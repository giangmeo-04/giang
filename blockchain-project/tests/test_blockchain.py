import unittest
from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_create_block(self):
        previous_hash = '0' * 64
        block = self.blockchain.create_block(previous_hash)
        self.assertEqual(block.index, 1)
        self.assertEqual(block.previous_hash, previous_hash)

    def test_add_transaction(self):
        transaction = Transaction('sender_address', 'recipient_address', 10)
        self.blockchain.add_transaction(transaction)
        self.assertEqual(len(self.blockchain.current_transactions), 1)

    def test_mine_block(self):
        previous_hash = '0' * 64
        self.blockchain.create_block(previous_hash)
        self.blockchain.add_transaction(Transaction('sender_address', 'recipient_address', 10))
        mined_block = self.blockchain.mine_block()
        self.assertEqual(mined_block.index, 2)
        self.assertEqual(len(mined_block.transactions), 1)

    def test_validate_chain(self):
        self.blockchain.create_block('0' * 64)
        self.blockchain.create_block('1' * 64)
        self.assertTrue(self.blockchain.validate_chain())

    def test_invalid_chain(self):
        self.blockchain.create_block('0' * 64)
        self.blockchain.chain[1].previous_hash = 'invalid_hash'
        self.assertFalse(self.blockchain.validate_chain())

if __name__ == '__main__':
    unittest.main()