import unittest
from blockchain.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction("Alice", "Bob", 50)

    def test_transaction_initialization(self):
        self.assertEqual(self.transaction.sender, "Alice")
        self.assertEqual(self.transaction.recipient, "Bob")
        self.assertEqual(self.transaction.amount, 50)

    def test_transaction_repr(self):
        expected_repr = f"Transaction(sender=Alice, recipient=Bob, amount=50)"
        self.assertEqual(repr(self.transaction), expected_repr)

    def test_transaction_invalid_amount(self):
        with self.assertRaises(ValueError):
            Transaction("Alice", "Bob", -10)

    def test_transaction_invalid_sender(self):
        with self.assertRaises(ValueError):
            Transaction("", "Bob", 50)

    def test_transaction_invalid_recipient(self):
        with self.assertRaises(ValueError):
            Transaction("Alice", "", 50)

if __name__ == '__main__':
    unittest.main()