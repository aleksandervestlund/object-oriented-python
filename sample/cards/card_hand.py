from card import Card
from card_container_impl import CardContainerImpl


class CardHand(CardContainerImpl):
    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def play(self) -> Card:
        return self.cards.pop(0)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
