from collections.abc import Callable, Iterator
from typing import Self


class BinaryComputingIterator:
    def __init__(
        self,
        iterator_1: Iterator[float],
        iterator_2: Iterator[float],
        operator: Callable[[float, float], float],
        *,
        default_1: float | None = None,
        default_2: float | None = None,
    ) -> None:
        self.iterator_1 = iterator_1
        self.iterator_2 = iterator_2
        self.operator = operator
        self.default_1 = default_1
        self.default_2 = default_2

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> float:
        it_1 = next(self.iterator_1, self.default_1)
        it_2 = next(self.iterator_2, self.default_2)

        if it_1 is None or it_2 is None:
            raise StopIteration

        return self.operator(it_1, it_2)  # type: ignore


def main() -> None:
    bci = BinaryComputingIterator(
        iter([1.0, 2.0, 3.0]),
        iter([4.0, 5.0, 6.0, 7.0]),
        lambda x, y: x + y,
        default_1=0,
    )

    for _ in range(4):
        print(next(bci))
    try:
        print(next(bci))
    except StopIteration:
        print("StopIteration")


if __name__ == "__main__":
    main()
