from abc import ABC, abstractmethod


class AbstractAccount(ABC):
    def __init__(self) -> None:
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        if amount <= 0.0:
            raise ValueError("Amount must be positive.")

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        self.internal_withdraw(amount)

    @abstractmethod
    def internal_withdraw(self, amount: float) -> None:
        pass
