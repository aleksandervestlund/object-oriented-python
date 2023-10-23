from account import Account


class SavingsAccount(Account):
    def __init__(self, interest_rate: float) -> None:
        if not 0 <= interest_rate <= 1.0:
            raise ValueError("Interest rate must be between 0.0 and 1.0.")

        self.balance: float = 0.0
        self.interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        if amount <= 0.0:
            raise ValueError("Amount must be positive.")

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0.0 or amount > self.balance:
            raise ValueError(
                "Amount must be positive and smaller than balance."
            )

        self.balance -= amount

    def end_year_update(self) -> None:
        self.balance *= 1 + self.interest_rate
