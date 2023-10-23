SUITS = ("S", "H", "D", "C")


class Card:
    def __init__(self, suit: str, face: int) -> None:
        if suit not in SUITS:
            raise ValueError(f"Suit must be either: {', '.join(SUITS)}.")
        if not 0 < face <= 13:
            raise ValueError("Face must be between 1 and 13 (inclusively).")

        self.suit = suit
        self.face = face

    def __repr__(self) -> str:
        return self.suit + str(self.face)


def main() -> None:
    c1 = Card("C", 1)
    print(c1)


if __name__ == "__main__":
    main()
