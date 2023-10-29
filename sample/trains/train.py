from cargo_car import CargoCar
from passenger_car import PassengerCar
from train_car import TrainCar


class Train:
    def __init__(self) -> None:
        self.train_cars: list[TrainCar] = []

    def add_train_car(self, train_car: TrainCar) -> None:
        self.train_cars.append(train_car)

    def contains(self, train_car: TrainCar) -> bool:
        return train_car in self.train_cars

    def get_total_weight(self) -> int:
        return sum(
            train_car.get_total_weight() for train_car in self.train_cars
        )

    def get_passenger_count(self) -> int:
        return sum(
            train_car.passenger_count
            for train_car in self.train_cars
            if isinstance(train_car, PassengerCar)
        )

    def get_cargo_weight(self) -> int:
        return sum(
            train_car.cargo_weight
            for train_car in self.train_cars
            if isinstance(train_car, CargoCar)
        )

    def __repr__(self) -> str:
        return str(self.train_cars)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
