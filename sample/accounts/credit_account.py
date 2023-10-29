from abstract_account import AbstractAccount


class DebitAccount(AbstractAccount):
    def __init__(self, credit_line: float) -> None:
        super().__init__()
        self._credit_line = credit_line

    @property
    def credit_line(self) -> float:
        return self._credit_line

    @credit_line.setter
    def credit_line(self, credit_line: float) -> None:
        if credit_line < 0.0:
            raise ValueError("Credit line must be positive.")
        if self.balance < 0.0 and credit_line < -self.balance:
            raise ValueError("Credit line must be larger than current debt.")

        self._credit_line = credit_line

    def internal_withdraw(self, amount: float) -> None:
        if amount <= 0.0 or (amount - self.balance) > self.credit_line:
            raise ValueError(
                "Amount must be positive and amount cannot overstep credit line."
            )

        self.balance -= amount
