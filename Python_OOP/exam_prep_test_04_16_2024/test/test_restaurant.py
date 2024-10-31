from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Arkata", 100)

    def test_correct_innit(self):
        self.assertEqual("Arkata", self.restaurant.name)
        self.assertEqual(100, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_value_error_if_dont_have_passed_name(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ""

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_value_error_when_capacity_is_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1

        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_when_we_dont_have_min_and_max_earnings(self):
        self.restaurant.waiters = [{"Nikola": 40}]
        self.assertEqual([{"Nikola": 40}], self.restaurant.get_waiters())

    def test_when_we_have_min_and_max_values(self):
        self.restaurant.waiters = [{"name": "Nikola"}]
        self.assertEqual([], self.restaurant.get_waiters(20, 80))

    def test_return_string_when_we_have_full_capacity_in_add_waiter_method(self):
        self.restaurant.waiters = [{"name": "Nikola"}]
        self.restaurant.capacity = 1
        self.assertEqual("No more places!", self.restaurant.add_waiter("Koko"))

    def test_if_we_have_the_same_waiter_in_waiters(self):
        self.restaurant.waiters = [{"name": "Nikola"}]
        self.assertEqual(f"The waiter Nikola already exists!", self.restaurant.add_waiter("Nikola"))

    def test_creating_new_waiter_and_adding_it_to_waiters(self):
        result = self.restaurant.add_waiter("Bobo")
        self.assertEqual([{"name": "Bobo"}], self.restaurant.waiters)
        self.assertEqual(f"The waiter Bobo has been added.", result)

    def test_removing_waiter_and_returning_message_of_it(self):
        self.restaurant.waiters = [{"name": "Nikola"}]
        result = self.restaurant.remove_waiter("Nikola")

        self.assertEqual([], self.restaurant.waiters)
        self.assertEqual(f"The waiter Nikola has been removed.", result)

    def test_returning_message_when_there_is_no_such_waiter_in_waiters(self):
        self.restaurant.waiters = [{"name": "Nikola"}]
        self.assertEqual(f"No waiter found with the name Bobo.", self.restaurant.remove_waiter("Bobo"))

    def test_get_the_sum_off_all_waiters_earnings(self):
        self.restaurant.waiters = [{"name": "Nikola", "total_earnings": 100}]
        self.assertEqual(100, self.restaurant.get_total_earnings())

if __name__ == "__main__":
    pass