from io import StringIO


class Nim:
    def __init__(self, pile_size: int = 10) -> None:
        self.piles = [[None for _ in range(pile_size)] for _ in range(3)]

    def remove_pieces(self, number: int, target_pile: int) -> None:
        if not self.is_valid_move(number, target_pile):
            raise ValueError("Illegal move.")

        for _ in range(number):
            self.piles[target_pile].pop()

    def is_valid_move(self, number: int, target_pile: int) -> bool:
        if number <= 0 or not 0 <= target_pile <= 2:
            return False
        return not any(len(pile) < number for pile in self.piles)

    def is_game_over(self) -> bool:
        return not all(pile for pile in self.piles)

    def get_pile(self, target_pile: int) -> int:
        return len(self.piles[target_pile])

    def __repr__(self) -> str:
        string = StringIO()
        for i in range(3):
            string.write(f"{i}: {self.get_pile(i)}. ")
        return string.getvalue()
