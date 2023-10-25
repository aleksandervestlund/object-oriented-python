from collections.abc import Iterator
from string_grids.string_grid import StringGrid


class StringGridIterator:
    def __init__(self, string_grid: StringGrid, row_major: bool) -> None:
        self.string_grid = string_grid
        self.row_major = row_major

        self.row_index = 0
        self.column_index = 0

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self):
        if (
            self.column_index == self.string_grid.get_column_count()
            or self.row_index == self.string_grid.get_row_count()
        ):
            raise StopIteration

        element = self.string_grid.get_element(
            self.row_index, self.column_index
        )

        if self.row_major:
            if self.column_index < self.string_grid.get_column_count():
                self.column_index += 1
            else:
                self.column_index = 0
                self.row_index += 1
        else:
            if self.row_index < self.string_grid.get_row_count():
                self.row_index += 1
            else:
                self.row_index = 0
                self.column_index += 1

        return element


def main() -> None:
    pass


if __name__ == "__main__":
    main()
