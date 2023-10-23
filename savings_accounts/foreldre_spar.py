from savings_account import SavingsAccount


class ForeldreSpar(SavingsAccount):
    def __init__(self, interest_rate: float, maximum_withdrawals: int) -> None:
        super().__init__(interest_rate)
        if maximum_withdrawals < 0:
            raise ValueError("Amount of withdrawals must be positive.")

        self.maximum_withdrawals = maximum_withdrawals
        self.remaining_withdrawals = maximum_withdrawals

    def deposit(self, amount: float) -> None:
        if self.remaining_withdrawals - 1 < 0:
            raise ValueError("Reached maximum withdrawals.")

        super().deposit(amount)
        self.remaining_withdrawals -= 1

    def end_year_update(self) -> None:
        super().end_year_update()
        self.remaining_withdrawals = self.maximum_withdrawals
