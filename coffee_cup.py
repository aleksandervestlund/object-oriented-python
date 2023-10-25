def is_valid_capacity(capacity: float) -> bool:
    return capacity >= 0.0


class CoffeeCup:
    def __init__(
        self, capacity: float = 0.0, current_volume: float = 0.0
    ) -> None:
        if not is_valid_capacity(capacity):
            raise ValueError("Illegal capacity given.")
        if not self.is_valid_volume(current_volume):
            raise ValueError("Illegal volume given.")

        self.capacity = capacity
        self.current_colume = current_volume

    def is_valid_volume(self, volume: float) -> bool:
        return 0.0 <= volume <= self.capacity

    def increase_cup_size(self, bigger_capacity: float) -> None:
        if is_valid_capacity(bigger_capacity):
            self.capacity += bigger_capacity

    def can_drink(self, volume: float) -> bool:
        return self.current_colume >= volume

    def drink_coffee(self, volume: float) -> None:
        if not self.can_drink(volume) or not self.is_valid_volume(volume):
            raise ValueError("You can't drink that much coffee!")

        self.current_colume -= volume

    def fill_coffee(self, volume: float) -> None:
        if not self.is_valid_volume(self.current_colume + volume):
            raise ValueError(
                "You just poured coffee all over the table. Good job."
            )

        self.current_colume += volume


def main() -> None:
    pass


if __name__ == "__main__":
    main()
