import string


CHARACTERS = string.digits + string.ascii_uppercase


class Digit:
    def __init__(self, base: int) -> None:
        if not 1 < base <= len(CHARACTERS):
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
        return CHARACTERS[self.value % self.base]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
