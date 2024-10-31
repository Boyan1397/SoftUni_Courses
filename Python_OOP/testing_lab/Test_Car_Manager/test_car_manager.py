from unittest import TestCase, main

from Python_OOP.testing_lab.Test_Car_Manager.car_manager import Car


class TestCarManager(TestCase):

    def setUp(self):
        self.car = Car("Audi", "Q7", 10, 100)

    def test_the_innit_method(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("Q7", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_exception_if_empty_string_in_make_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_the_exception_if_empty_string_in_model_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_the_exception_if_consumption_is_below_or_equal_to_zero_in_consumption_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_the_exception_if_capacity_is_below_or_equal_to_zero_capacity_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_the_exception_if_amount_is_below_zero_in_amount_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_the_fuel_is_below_or_equal_to_zero_in_refuel_method(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_if_we_are_setting_the_f_capacity_to_f_amount_if_amount_is_bigger_than_capacity(self):
        self.car.fuel_amount = 100

        self.car.refuel(10)

        self.assertEqual(100, self.car.fuel_amount)

    def test_exception_when_needed_is_bigger_than_fuel_amount_in_drive_method(self):

        with self.assertRaises(Exception) as ex:
            self.car.drive(80)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_when_we_have_enough_fuel_to_drive(self):
        self.car.fuel_amount = 1000

        self.car.drive(8)

        self.assertEqual(999.2, self.car.fuel_amount)





if __name__ == "__main__":
    main()

