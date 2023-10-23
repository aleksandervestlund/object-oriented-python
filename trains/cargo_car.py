from train_car import TrainCar


class CargoCar(TrainCar):
    def __init__(self, dead_weight: int, cargo_weight: int) -> None:
        super().__init__(dead_weight)
        self._cargo_weight = cargo_weight

    @property
    def cargo_weight(self) -> int:
        return self._cargo_weight

    @cargo_weight.setter
    def cargo_weight(self, cargo_weight: int) -> None:
        if cargo_weight < 0:
            raise ValueError("Weight cannot be negative.")
        self._cargo_weight = cargo_weight

    def get_total_weight(self) -> int:
        return super().get_total_weight() + self._cargo_weight

    def __repr__(self) -> str:
        return (
            f"Cargo Car(Weight: {self.get_total_weight()}, Cargo: "
            f"{self._cargo_weight} kg)"
        )
