def _check_non_negative(amount: float) -> None:
    if amount < 0:
        raise ValueError("Value must be non-negative.")


class Account:
    def __init__(self, balance: float, interest_rate: float) -> None:
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        _check_non_negative(amount)
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        _check_non_negative(amount)
        self.balance -= amount

    def update_interest(self) -> None:
        self.balance *= 1 + self.interest_rate

    def set_interest_rate(self, interest_rate: float) -> None:
        _check_non_negative(interest_rate)
        self.interest_rate = interest_rate


def main() -> None:
    acc = Account(1000, 0.01)
    acc.deposit(1000)
    print(acc.balance)  # Skal være 2000
    acc.withdraw(500)
    print(acc.balance)  # Skal være 1500
    acc.update_interest()
    print(acc.balance)  # Skal være 1515.0


if __name__ == "__main__":
    main()
