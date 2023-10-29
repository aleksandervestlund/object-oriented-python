class TrainCar:
    def __init__(self, dead_weight: int) -> None:
        self._dead_weight = dead_weight

    @property
    def dead_weight(self) -> int:
        return self._dead_weight

    @dead_weight.setter
    def dead_weight(self, dead_weight: int) -> None:
        if dead_weight < 0:
            raise ValueError("Weight cannot be negative.")

        self._dead_weight = dead_weight

    def get_total_weight(self) -> int:
        return self._dead_weight

    def __repr__(self) -> str:
        return f"Train Car(Weight: {self.get_total_weight()})"


def main() -> None:
    pass


if __name__ == "__main__":
    main()
