from sample.cards.card import SUITS, Card
from sample.cards.card_container import CardContainer
from sample.cards.card_hand import CardHand


class CardDeck(CardContainer):
    def __init__(self, n: int) -> None:
        super().__init__()
        if not 0 <= n <= 13:
            raise ValueError("Invalid amunt of faces.")

        self.cards.extend(
            [Card(suit, face) for suit in SUITS for face in range(1, n + 1)]
        )

    def shuffle_perfectly(self) -> None:
        temp_cards: list[Card] = []

        middle = self.get_card_count() // 2  # Length will never be odd
        for i in range(middle):
            temp_cards.append(self.get_card(i))
            temp_cards.append(self.get_card(middle + i))

        self.cards = temp_cards

    def deal(self, card_hand: CardHand, n: int) -> None:
        for _ in range(n):
            card_hand.add_card(self.cards.pop())

    def __repr__(self) -> str:
        return str(self.cards)


def main() -> None:
    cd1 = CardDeck(2)
    print(cd1)
    cd1.shuffle_perfectly()
    print(cd1)


if __name__ == "__main__":
    main()
