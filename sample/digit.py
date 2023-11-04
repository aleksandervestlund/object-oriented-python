import string


class Digit:
    def __init__(self, base: int) -> None:
        if not 1 < base <= 36:
            raise ValueError("Base must be positive and smaller than 36.")

        self.base = base
        self.value = 0

    def increment(self) -> bool:
        self.value += 1
        if self.value == self.base:
            self.value = 0
            return True
        return False

    def __repr__(self) -> str:
        convert_string = string.digits + string.ascii_uppercase
        number = self.value % self.base
        return convert_string[number]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
