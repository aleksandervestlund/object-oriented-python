from unittest import TestCase

from sample.accounts.debit_account import DebitAccount


class DebitAccountTest(TestCase):
    def setUp(self) -> None:
        self.account = DebitAccount()

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
