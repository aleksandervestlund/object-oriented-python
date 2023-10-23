from enum import Enum, auto


class VehicleType(Enum):
    CAR = auto()
    MOTORCYCLE = auto()


class FuelType(Enum):
    GASOLINE = auto()
    DIESEL = auto()
    HYDROGEN = auto()
    ELECTRIC = auto()


class Vehicle:
    def __init__(
        self,
        vehicle_type: VehicleType,
        fuel_type: FuelType,
        registration_number: str,
    ) -> None:
        self.vehicle_type = vehicle_type
        self.fuel_type = fuel_type
        self._registration_number = registration_number

    @property
    def registration_number(self) -> str:
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number: str) -> None:
        registration_number = registration_number.upper()
        if self.fuel_type is FuelType.ELECTRIC:
            if not (
                registration_number.startswith("EK")
                or registration_number.startswith("EL")
            ):
                raise ValueError("Invalid registration number.")
        elif self.fuel_type is FuelType.HYDROGEN:
            if not registration_number.startswith("HY"):
                raise ValueError("Invalid registration number.")
        elif (
            registration_number.startswith("HY")
            or registration_number.startswith("EK")
            or registration_number.startswith("EL")
        ):
            raise ValueError("Invalid registration number.")

        if (
            self.vehicle_type is VehicleType.CAR
            and len(registration_number) != 7
        ):
            raise ValueError("Invalid length.")
        if (
            self.vehicle_type is VehicleType.MOTORCYCLE
            and len(registration_number) != 6
        ):
            raise ValueError("Invalid length.")

        if not registration_number[:2].isalpha():
            raise ValueError("Two first characters must be letters.")
        if not registration_number[2:].isdigit():
            raise ValueError("Last characters must be digits.")

        self._registration_number = registration_number
