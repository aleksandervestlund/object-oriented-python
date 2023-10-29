class Digit:
    def __init__(self, *, base: int, value: int) -> None:
        if not 0 < base <= 36:
            raise ValueError("Base must be positive and smaller than 36.")
        if not 0 < value < base:
            raise ValueError("Value must be positive and smaller than base")

        self.base = base
        self.value = value

    def increment(self) -> bool:
        self.value += 1
        if self.value == self.base:
            self.value = 0
            return True
        return False


def main() -> None:
    pass


if __name__ == "__main__":
    main()
