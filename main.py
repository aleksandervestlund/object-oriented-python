from sample.cards.card_deck import CardDeck


def main() -> None:
    cd1 = CardDeck(2)
    print(cd1)
    cd1.shuffle_perfectly()
    print(cd1)


if __name__ == "__main__":
    main()
