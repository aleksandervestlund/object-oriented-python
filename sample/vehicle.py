from enum import Enum, auto


class VehicleType(Enum):
    CAR = auto()
    MOTORCYCLE = auto()


class FuelType(Enum):
    DIESEL = auto()
    ELECTRIC = auto()
    GASOLINE = auto()
    HYDROGEN = auto()


class Vehicle:
    def __init__(
        self,
        vehicle_type: VehicleType,
        fuel_type: FuelType,
        registration_number: str,
    ) -> None:
        if not isinstance(vehicle_type, VehicleType):
            raise ValueError("Invalid vehicle type.")
        if not isinstance(fuel_type, FuelType):
            raise ValueError("Invalid fuel type.")
        if (
            vehicle_type is VehicleType.MOTORCYCLE
            and fuel_type is FuelType.HYDROGEN
        ):
            raise ValueError("Invalid combination.")

        self.vehicle_type = vehicle_type
        self.fuel_type = fuel_type
        self.registration_number = registration_number

    @property
    def registration_number(self) -> str:
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number: str) -> None:
        letters = registration_number[:2]
        digits = registration_number[2:]

        if not (letters.isalpha() and letters.isupper()):
            raise ValueError("Two first characters must be uppercase letters.")
        if not digits.isdigit():
            raise ValueError("Last characters must be digits.")
        if any(letter in letters for letter in "ÆØÅ"):
            raise ValueError("Letters must not be Æ, Ø or Å.")
        if self.vehicle_type is VehicleType.CAR and len(digits) != 5:
            raise ValueError("Registration number must be 5 digits for cars.")
        if self.vehicle_type is VehicleType.MOTORCYCLE and len(digits) != 4:
            raise ValueError(
                "Registration number must be 4 digits for motorcycles."
            )

        if self.fuel_type is FuelType.ELECTRIC:
            if not (letters == "EK" or letters == "EL"):
                raise ValueError("Invalid registration number.")
        elif self.fuel_type is FuelType.HYDROGEN:
            if letters != "HY":
                raise ValueError("Invalid registration number.")
        elif letters in {"HY", "EK", "EL"}:
            raise ValueError("Invalid registration number.")

        self._registration_number = registration_number


def main() -> None:
    pass


if __name__ == "__main__":
    main()
