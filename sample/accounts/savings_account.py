from abstract_account import AbstractAccount


class DebitAccount(AbstractAccount):
    def __init__(self, withdrawals: int, fee: float) -> None:
        super().__init__()
        if fee < 0.0 or withdrawals < 0:
            raise ValueError(
                "Both the amount of withdrawals and fee must be positive."
            )

        self.withdrawals = withdrawals
        self.fee = fee

    def internal_withdraw(self, amount: float) -> None:
        if amount <= 0.0 or amount > self.balance:
            raise ValueError(
                "Amount must be positive and smaller than balance."
            )
        if not self.withdrawals:
            if self.balance - amount - self.fee < 0.0:
                raise ValueError("Cannot afford fee.")

            self.balance -= self.fee

        self.balance -= amount
