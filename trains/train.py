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
        passenger_cars: list[PassengerCar] = []
        for train_car in self.train_cars:
            if isinstance(train_car, PassengerCar):
                passenger_cars.append(train_car)
        return sum(
            passenger_car.passenger_count for passenger_car in passenger_cars
        )

    def get_cargo_weight(self) -> int:
        cargo_cars: list[CargoCar] = []
        for train_car in self.train_cars:
            if isinstance(train_car, CargoCar):
                cargo_cars.append(train_car)
        return sum(cargo_car.cargo_weight for cargo_car in cargo_cars)

    def __repr__(self) -> str:
        return str(self.train_cars)
