from typing import Self

from card import Card
from card_container import CardContainer


class CardContainerIterator:
    def __init__(self, card_container: CardContainer) -> None:
        self.card_container = card_container
        self.index = 0

    def __next__(self) -> Card:
        if self.index >= self.card_container.get_card_count():
            raise StopIteration

        card = self.card_container.get_card(self.index)
        self.index += 1
        return card

    def __iter__(self) -> Self:
        return self


def main() -> None:
    pass


if __name__ == "__main__":
    main()
