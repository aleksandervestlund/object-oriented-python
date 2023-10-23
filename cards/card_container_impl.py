from card_container import CardContainer
from card import Card


class CardContainerImpl(CardContainer):
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def get_card_count(self) -> int:
        return len(self.cards)

    def get_card(self, n: int) -> Card:
        return self.cards[n]
