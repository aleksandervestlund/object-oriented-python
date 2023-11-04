class Location:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def up(self) -> None:
        self.y -= 1

    def down(self) -> None:
        self.y += 1

    def left(self) -> None:
        self.x -= 1

    def right(self) -> None:
        self.x += 1

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"


def main() -> None:
    pass


if __name__ == "__main__":
    main()
