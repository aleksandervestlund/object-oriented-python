from unittest import TestCase

from sample.accounts.savings_account import SavingsAccount


class SavingsAccountTest(TestCase):
    def setUp(self):
        self.account = SavingsAccount(1, 50.0)

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

        with self.assertRaises(ValueError):
            self.account.withdraw(20000.0)

        self.assertEqual(15000.0, self.account.balance)
        self.account.withdraw(10000.0)
        self.assertEqual(4950.0, self.account.balance)

        with self.assertRaises(ValueError):
            self.account.withdraw(4930.0)

        self.assertEqual(4950.0, self.account.balance)
