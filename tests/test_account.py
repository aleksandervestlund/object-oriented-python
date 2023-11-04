from unittest import TestCase
from sample.account import Account


class TestAccount(TestCase):
    def setUp(self) -> None:
        self.account = Account()

    def test_init(self) -> None:
        self.assertEqual(self.account.balance, 0.0)
        self.assertEqual(self.account.interest_rate, 0.0)

        with self.assertRaises(ValueError):
            Account(balance=-1.0)
        with self.assertRaises(ValueError):
            Account(interest_rate=-1.0)

    def test_set_interest_rate(self) -> None:
        self.account.interest_rate = 0.5
        self.assertEqual(self.account.interest_rate, 0.5)

        with self.assertRaises(ValueError):
            self.account.interest_rate = -1.0
        with self.assertRaises(ValueError):
            self.account.interest_rate = 1.1

    def test_deposit(self) -> None:
        self.account.deposit(1.0)
        self.assertEqual(self.account.balance, 1.0)

        with self.assertRaises(ValueError):
            self.account.deposit(-1.0)

    def test_withdraw(self) -> None:
        self.account.deposit(1.0)
        self.account.withdraw(1.0)
        self.assertEqual(self.account.balance, 0.0)

        with self.assertRaises(ValueError):
            self.account.withdraw(-1.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(1.0)

    def test_add_interest(self) -> None:
        self.account.deposit(1.0)
        self.account.interest_rate = 1.0
        self.account.add_interest()
        self.assertEqual(self.account.balance, 2.0)
