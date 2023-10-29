from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
