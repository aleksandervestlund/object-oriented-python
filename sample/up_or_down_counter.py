class UpOrDownCounter:
    def __init__(self, start: int, end: int) -> None:
        if start == end:
            raise ValueError("Start must be different from end.")
        self.counter = start
        self.end = end
        self.direction = 1 if start < end else -1

    def count(self) -> bool:
        if self.counter == self.end:
            return False
        self.counter += self.direction
        return self.counter != self.end


def main() -> None:
    pass


if __name__ == "__main__":
    main()
