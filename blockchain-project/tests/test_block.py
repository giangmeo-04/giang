import unittest
from blockchain.block import Block
import time

class TestBlock(unittest.TestCase):

    def setUp(self):
        self.index = 1
        self.timestamp = time.time()
        self.transactions = []
        self.previous_hash = '0' * 64
        self.block = Block(self.index, self.timestamp, self.transactions, self.previous_hash)

    def test_block_initialization(self):
        self.assertEqual(self.block.index, self.index)
        self.assertEqual(self.block.timestamp, self.timestamp)
        self.assertEqual(self.block.transactions, self.transactions)
        self.assertEqual(self.block.previous_hash, self.previous_hash)

    def test_block_hash(self):
        self.assertIsNotNone(self.block.hash)
        self.assertEqual(len(self.block.hash), 64)

    def test_block_string_representation(self):
        expected_string = f"Block(index={self.index}, timestamp={self.timestamp}, transactions={self.transactions}, previous_hash={self.previous_hash}, hash={self.block.hash})"
        self.assertEqual(str(self.block), expected_string)

if __name__ == '__main__':
    unittest.main()