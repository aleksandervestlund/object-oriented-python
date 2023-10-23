from train_car import TrainCar


class PassengerCar(TrainCar):
    def __init__(self, dead_weight: int, passenger_count: int) -> None:
        super().__init__(dead_weight)
        self._passenger_count = passenger_count

    @property
    def passenger_count(self) -> int:
        return self._passenger_count

    @passenger_count.setter
    def passenger_count(self, passenger_count: int) -> None:
        if passenger_count < 0:
            raise ValueError("Passenger count cannot be negative.")
        self._passenger_count = passenger_count

    def get_total_weight(self) -> int:
        return super().get_total_weight() + self._passenger_count * 80

    def __repr__(self) -> str:
        return (
            f"Passenger Car(Weight: {self.get_total_weight()}, Passengers: "
            f"{self._passenger_count})"
        )
