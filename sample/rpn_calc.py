from collections.abc import Callable


class RPNCalc:
    def __init__(self) -> None:
        self.stack: list[float] = []
        self.operators: dict[str, Callable[[float, float], float]] = {}

    def push(self, value: float) -> None:
        self.stack.insert(0, value)

    def pop(self) -> float:
        if len(self.stack) == 0:
            return float("nan")
        return self.stack.pop(0)

    def peek(self, n: int) -> float:
        if not 0 <= n < len(self.stack):
            return float("nan")
        return self.stack[n]

    def get_size(self) -> int:
        return len(self.stack)

    def add_operator(
        self, symbol: str, operator: Callable[[float, float], float]
    ) -> bool:
        if symbol in self.operators:
            return False

        self.operators[symbol] = operator
        return True

    def remove_operator(self, symbol: str) -> None:
        if symbol not in self.operators:
            raise ValueError(f"Operator '{symbol}' does not exist.")

        del self.operators[symbol]

    def perform_operation(self, symbol: str) -> None:
        if symbol not in self.operators:
            raise ValueError(f"Operator '{symbol}' does not exist.")

        first_element = self.pop()
        next_element = self.pop()
        result = self.operators[symbol](next_element, first_element)
        self.push(result)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
