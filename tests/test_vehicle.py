from unittest import TestCase

from sample.vehicle import FuelType, Vehicle, VehicleType


class VehicleTest(TestCase):
    def _check_vehicle_state(
        self,
        vehicle_type: VehicleType,
        fuel_type: FuelType,
        registration_number: str,
        vehicle: Vehicle,
    ) -> None:
        self.assertIs(vehicle_type, vehicle.vehicle_type)
        self.assertIs(fuel_type, vehicle.fuel_type)
        self.assertEqual(registration_number, vehicle.registration_number)

    def _check_invalid_constructor(
        self,
        vehicle_type: VehicleType,
        fuel_type: FuelType,
        registration_number: str,
    ) -> None:
        with self.assertRaises(ValueError):
            Vehicle(vehicle_type, fuel_type, registration_number)

    def _check_invalid_registration(
        self,
        vehicle: Vehicle,
        original_registration_num: str,
        new_registration_number: str,
    ) -> None:
        with self.assertRaises(ValueError):
            vehicle.registration_number = new_registration_number
        self.assertEqual(
            original_registration_num, vehicle.registration_number
        )

    def test_constructor(self) -> None:
        vehicle = Vehicle(VehicleType.CAR, FuelType.DIESEL, "BN12345")
        self._check_vehicle_state(
            VehicleType.CAR, FuelType.DIESEL, "BN12345", vehicle
        )

        vehicle = Vehicle(VehicleType.MOTORCYCLE, FuelType.ELECTRIC, "EL1234")
        self._check_vehicle_state(
            VehicleType.MOTORCYCLE, FuelType.ELECTRIC, "EL1234", vehicle
        )
        self._check_invalid_constructor(VehicleType.CAR, "Y", "BN12345")  # type: ignore
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.HYDROGEN, "HY1234"
        )
        self._check_invalid_constructor("P", FuelType.DIESEL, "BN12345")  # type: ignore
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "A1234"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "A12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "A123456"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "A12344"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "AÆ12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "ab12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "A12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "A1B12345"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.GASOLINE, "A1234"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.GASOLINE, "A12345"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.GASOLINE, "A123"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.GASOLINE, "AB12345"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.GASOLINE, "ABC1234"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.GASOLINE, "ABC12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "AÅ1234"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "ab1234"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "EL12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "EK12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.GASOLINE, "HY12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.DIESEL, "EL12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.DIESEL, "EK12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.DIESEL, "HY12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.HYDROGEN, "EL12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.HYDROGEN, "EK12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.HYDROGEN, "BN12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.ELECTRIC, "HY12345"
        )
        self._check_invalid_constructor(
            VehicleType.CAR, FuelType.ELECTRIC, "BN12345"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.GASOLINE, "EL1234"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.GASOLINE, "EK1234"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.GASOLINE, "HY1234"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.DIESEL, "EL1234"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.DIESEL, "EK1234"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.DIESEL, "HY1234"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.ELECTRIC, "HY1234"
        )
        self._check_invalid_constructor(
            VehicleType.MOTORCYCLE, FuelType.ELECTRIC, "BN1234"
        )

    def test_registration_number(self) -> None:
        vehicle = Vehicle(VehicleType.CAR, FuelType.DIESEL, "BN12345")
        vehicle.registration_number = "AB54321"
        self._check_vehicle_state(
            VehicleType.CAR, FuelType.DIESEL, "AB54321", vehicle
        )

        vehicle = Vehicle(VehicleType.MOTORCYCLE, FuelType.ELECTRIC, "EK1234")
        vehicle.registration_number = "EL4321"
        self._check_vehicle_state(
            VehicleType.MOTORCYCLE, FuelType.ELECTRIC, "EL4321", vehicle
        )

        vehicle = Vehicle(VehicleType.CAR, FuelType.DIESEL, "BN12345")
        with self.assertRaises(ValueError):
            vehicle.registration_number = "A1234"
        self._check_vehicle_state(
            VehicleType.CAR, FuelType.DIESEL, "BN12345", vehicle
        )

        vehicle = Vehicle(VehicleType.MOTORCYCLE, FuelType.ELECTRIC, "EL1234")
        with self.assertRaises(ValueError):
            vehicle.registration_number = "HY1234"
        self._check_vehicle_state(
            VehicleType.MOTORCYCLE, FuelType.ELECTRIC, "EL1234", vehicle
        )

        vehicle = Vehicle(VehicleType.CAR, FuelType.GASOLINE, "AB12345")
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "A1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "A12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "AB1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "AB123456"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "ABC1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "AÆ12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "ab12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "A1B2345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "A1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "A12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "AB1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "AB123456"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "ABC1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "AÆ12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "ab12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "A1B2345"
        )

        vehicle = Vehicle(VehicleType.MOTORCYCLE, FuelType.GASOLINE, "AB1234")
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "A1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "A12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "AB123"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "AB12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "ABC1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "ABC12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "AÅ1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "ab1234"
        )

        vehicle = Vehicle(VehicleType.CAR, FuelType.GASOLINE, "AB12345")
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EL12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EK12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "HY12345"
        )

        vehicle = Vehicle(VehicleType.CAR, FuelType.DIESEL, "AB12345")
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EL12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EK12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "HY12345"
        )

        vehicle = Vehicle(VehicleType.CAR, FuelType.HYDROGEN, "HY12345")
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EL12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EK12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "BN12345"
        )

        vehicle = Vehicle(VehicleType.CAR, FuelType.ELECTRIC, "EL12345")
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "HY12345"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "BN12345"
        )

        vehicle = Vehicle(VehicleType.MOTORCYCLE, FuelType.GASOLINE, "AB1234")
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EL1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EK1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "HY1234"
        )
        vehicle = Vehicle(VehicleType.MOTORCYCLE, FuelType.DIESEL, "AB1234")
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EL1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "EK1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "HY1234"
        )

        vehicle = Vehicle(VehicleType.MOTORCYCLE, FuelType.ELECTRIC, "EK1234")
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "HY1234"
        )
        self._check_invalid_registration(
            vehicle, vehicle.registration_number, "BN1234"
        )
