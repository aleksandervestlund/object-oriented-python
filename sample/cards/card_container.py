from collections.abc import Iterator
from typing import Self

from sample.cards.card import Card


class CardContainer:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def get_card_count(self) -> int:
        return len(self.cards)

    def get_card(self, n: int) -> Card:
        return self.cards[n]

    def __iter__(self) -> Iterator[Card]:
        return CardContainerIterator(self)


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
