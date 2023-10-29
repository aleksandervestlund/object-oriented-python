from collections.abc import Iterator
from string_grid import StringGrid
from string_grid_iterator import StringGridIterator


class StringGridImpl(StringGrid):
    def __init__(self, rows: int, columns: int) -> None:
        self.grid = [["" for _ in range(columns)] for _ in range(rows)]

    def __iter__(self) -> Iterator[str]:
        return StringGridIterator(self, True)

    def get_row_count(self) -> int:
        return len(self.grid)

    def get_column_count(self) -> int:
        return len(self.grid[0])

    def get_element(self, row: int, column: int) -> str:
        if not 0 <= row < self.get_row_count():
            raise ValueError("Row out of range")
        if not 0 <= column < self.get_column_count():
            raise ValueError("Column out of range")

        return self.grid[row][column]

    def set_element(self, row: int, column: int, element: str) -> None:
        if not 0 <= row < self.get_row_count():
            raise ValueError("Row out of range")
        if not 0 <= column < self.get_column_count():
            raise ValueError("Column out of range")

        self.grid[row][column] = element


def main() -> None:
    pass


if __name__ == "__main__":
    main()
