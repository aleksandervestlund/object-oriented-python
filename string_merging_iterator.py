from collections.abc import Iterator


class StringMergingIterator:
    def __init__(self, first: Iterator[str], second: Iterator[str]) -> None:
        self.first = first
        self.second = second

        self.turn_switch = True

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.turn_switch:
            try:
                result = next(self.first)
            except StopIteration:
                result = next(self.second)

            self.turn_switch = False
        else:
            try:
                result = next(self.second)
            except StopIteration:
                result = next(self.first)

            self.turn_switch = True

        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
