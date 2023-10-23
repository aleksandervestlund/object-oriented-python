from abstract_account import AbstractAccount


class DebitAccount(AbstractAccount):
    def internal_withdraw(self, amount: float) -> None:
        if amount <= 0.0 or amount > self.balance:
            raise ValueError(
                "Amount must be positive and smaller than balance."
            )
        self.balance -= amount
