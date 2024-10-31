from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50.5, 200)

    def test_innit_correctness(self):
        self.assertEqual(50.5, self.vehicle.fuel)
        self.assertEqual(50.5, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_exception_error_when_we_dont_have_enough_fuel_in_drive_method(self):
        self.vehicle.fuel = 5

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(15)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_fuel_value_when_fuel_is_more_than_needed_fuel_in_drive_method(self):
        expected_fuel = 31.75

        self.vehicle.drive(15)

        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_exception_error_when_we_dont_have_enough_capacity_for_the_fuel_we_want_to_add_in_refuel_method(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50.5)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_when_we_have_enough_capacity_for_the_additional_fuel_in_refuel_method(self):
        self.vehicle.capacity = 150.5
        expected_fuel = 101.0

        self.vehicle.refuel(50.5)

        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_the_string_representation_in_str_method_(self):
        result = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        self.assertEqual(result, self.vehicle.__str__())





if __name__ == "__main__":
    main()