import unittest

from sample.accounts.credit_account import CreditAccount


class CreditAccountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = CreditAccount(10000.0)

    def test_deposit(self) -> None:
        self.assertEqual(0.0, self.account.balance)
        self.account.deposit(10000.0)
        self.assertEqual(10000.0, self.account.balance)

        with self.assertRaises(ValueError):
            self.account.deposit(-10000.0)

        self.assertEqual(10000.0, self.account.balance)

    def test_withdraw(self) -> None:
        self.account.deposit(20000.0)
        self.account.withdraw(5000.0)
        self.assertEqual(15000.0, self.account.balance)

        with self.assertRaises(ValueError):
            self.account.withdraw(-10000.0)

        self.assertEqual(15000.0, self.account.balance)
        self.account.withdraw(20000.0)
        self.assertEqual(-5000.0, self.account.balance)

        with self.assertRaises(ValueError):
            self.account.withdraw(20000.0)

    def test_credit_line(self) -> None:
        self.assertEqual(10000.0, self.account.credit_line)
        self.account.credit_line = 5000.0
        self.assertEqual(5000.0, self.account.credit_line)

        with self.assertRaises(ValueError):
            self.account.credit_line = -5000.0

        self.assertEqual(5000.0, self.account.credit_line)
        self.account.withdraw(4000.0)

        with self.assertRaises(ValueError):
            self.account.credit_line = 3000.0

        self.assertEqual(-4000.0, self.account.balance)
        self.assertEqual(5000.0, self.account.credit_line)
