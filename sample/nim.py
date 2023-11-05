from io import StringIO


class Nim:
    def __init__(self, pile_size: int) -> None:
        self.piles = [pile_size for _ in range(3)]

    def remove_pieces(self, number: int, target_pile: int) -> None:
        if not self.is_valid_move(number, target_pile):
            raise ValueError("Illegal move.")

        self.piles[target_pile] -= number

    def is_valid_move(self, number: int, target_pile: int) -> bool:
        return (
            not self.is_game_over()
            and 0 <= target_pile < 3
            and 0 < number <= self.piles[target_pile]
        )

    def is_game_over(self) -> bool:
        return not all(pile for pile in self.piles)

    def get_pile(self, target_pile: int) -> int:
        return self.piles[target_pile]

    def __repr__(self) -> str:
        string = StringIO()
        for i in range(3):
            string.write(f"{i}: {self.get_pile(i)}. ")
        return string.getvalue()


def main() -> None:
    pass


if __name__ == "__main__":
    main()
