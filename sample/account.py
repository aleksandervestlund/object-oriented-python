class Account:
    def __init__(
        self, *, balance: float = 0.0, interest_rate: float = 0.0
    ) -> None:
        if balance < 0.0:
            raise ValueError("Balance must be positive.")
        if not 0.0 <= interest_rate <= 1.0:
            raise ValueError("Interest rate must be between 0.0 and 1.0.")

        self.balance = balance
        self._interest_rate = interest_rate

    @property
    def interest_rate(self) -> float:
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate: float) -> None:
        if not 0.0 <= interest_rate <= 1.0:
            raise ValueError("Interest rate must be between 0.0 and 1.0.")

        self._interest_rate = interest_rate

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

    def add_interest(self) -> None:
        self.balance += self.balance * self._interest_rate

    def __repr__(self) -> str:
        return f"Balance: {self.balance}. Interest rate: {self.interest_rate}"


def main() -> None:
    a_1 = Account(balance=0, interest_rate=0.5)
    print(a_1.interest_rate)
    a_1.interest_rate = 0.6
    print(a_1.interest_rate)


if __name__ == "__main__":
    main()
