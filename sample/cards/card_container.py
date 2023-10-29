from abc import ABC, abstractmethod

from card import Card


class CardContainer(ABC):
    @abstractmethod
    def get_card_count(self) -> int:
        pass

    @abstractmethod
    def get_card(self, n: int) -> Card:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
