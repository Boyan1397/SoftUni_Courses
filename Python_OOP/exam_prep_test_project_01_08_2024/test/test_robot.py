from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("1397","Military", 100, 200)

    def test_correct_innit(self):
        self.assertEqual("1397", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(200, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_value_error_in_the_setter_if_the_value_is_not_in_the_allowed_ones(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "BlaBla"

        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_value_error_when_we_have_negative_price_given(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_check_if_the_component_is_in_the_upgrades_and_check_the_results(self):
        self.robot.hardware_upgrades = ["component"]

        self.robot.upgrade("component", 50)

        self.assertEqual(f"Robot {self.robot.robot_id} was not upgraded.", self.robot.upgrade("component", 50))

    def test_if_we_are_adding_and_appending_correctly_when_we_dont_have_the_component_in_upgrades(self):
        self.robot.upgrade("component", 50)
        self.assertEqual(["component"], self.robot.hardware_upgrades)
        self.assertEqual(275.0 , self.robot.price)

    def test_the_returned_string_when_we_dont_have_the_component_in_upgrades(self):
        result = self.robot.upgrade("component", 50)
        self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with component.', result)

    def test_software_updates_exist_and_max_software_updates_are_bigger_than_version(self):
        self.robot.software_updates = [200]
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", self.robot.update(100.0, 3))

    def test_when_needed_capacity_is_more_than_the_available_message(self):
        self.robot.software_updates = [1]

        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", self.robot.update(50, 300))

    def test_when_version_is_bigger_and_needed_capacity_is_smaller(self):
        self.robot.update(7777, 50)

        self.assertEqual([7777], self.robot.software_updates)
        self.assertEqual(50, self.robot.available_capacity)

    def test_the_return_string(self):
        result = self.robot.update(7777, 50)

        self.assertEqual(f'Robot {self.robot.robot_id} was updated to version 7777.', result)

    def test_the_return_when_the_price_is_bigger_than_the_other_price(self):
        other = Robot("1104", "Education", 70, 50)
        self.assertEqual(f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {other.robot_id}.', self.robot.__gt__(other))

    def test_the_return_when_the_price_is_equal_as_other_price(self):
        other = Robot("1104", "Education", 70, 200)
        self.assertEqual(f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {other.robot_id}.', self.robot.__gt__(other))

    def test_the_return_when_the_price_is_smaller_than_other_price(self):
        other = Robot("1104", "Education", 70, 10000)
        self.assertEqual(f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {other.robot_id}.', self.robot.__gt__(other))


if __name__ == "__main__":
    main()