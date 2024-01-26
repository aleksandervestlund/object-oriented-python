from sample.savings_accounts.savings_account import SavingsAccount


class BSU(SavingsAccount):
    def __init__(self, interest_rate: float, yearly_maximum: float) -> None:
        super().__init__(interest_rate)
        self.total_deposited = 0.0
        self.yearly_maximum = yearly_maximum

    def get_tax_deduction(self) -> float:
        return self.total_deposited * 0.2

    def deposit(self, amount: float) -> None:
        if self.balance + amount > self.yearly_maximum:
            raise ValueError("Cannot deposit that much.")

        super().deposit(amount)
        self.total_deposited += amount

    def end_year_update(self) -> None:
        super().end_year_update()
        self.total_deposited = 0


def main() -> None:
    pass


if __name__ == "__main__":
    main()
