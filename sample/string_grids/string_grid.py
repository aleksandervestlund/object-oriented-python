from abc import ABC, abstractmethod


class StringGrid(ABC):
    @abstractmethod
    def get_row_count(self) -> int:
        pass

    @abstractmethod
    def get_column_count(self) -> int:
        pass

    @abstractmethod
    def get_element(self, row: int, column: int) -> str:
        pass

    @abstractmethod
    def set_element(self, row: int, column: int, element: str) -> None:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
