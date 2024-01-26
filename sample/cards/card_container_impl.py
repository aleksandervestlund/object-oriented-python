from collections.abc import Iterator
from sample.cards.card import Card
from sample.cards.card_container import CardContainer


class CardContainerImpl(CardContainer):
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def get_card_count(self) -> int:
        return len(self.cards)

    def get_card(self, n: int) -> Card:
        return self.cards[n]

    def __iter__(self) -> Iterator[Card]:
        return iter(self.cards)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
