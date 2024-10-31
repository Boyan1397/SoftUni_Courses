from collections import deque
from unittest import TestCase, main

from Python_OOP.exam_prep_test_09_12_2023.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("Lora")
        self.station.arrival_trains = deque(["Bobo"])
        self.station.departure_trains = deque(["Toni"])

    def test_is_innit_correct(self):
        self.assertEqual("Lora", self.station.name)
        self.assertEqual(deque(["Bobo"]), self.station.arrival_trains)
        self.assertEqual(deque(["Toni"]), self.station.departure_trains)

    def test_name_value_error_when_name_length_is_below_three_chars(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Kur"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_appending_correctly_in_arrival_trains(self):
        expected_arrivals = deque(["Bobo", "Djani"])

        self.station.new_arrival_on_board("Djani")

        self.assertEqual(expected_arrivals, self.station.arrival_trains)

    def test_returning_message_when_we_have_different_first_train(self):

        self.assertEqual(f"There are other trains to arrive before Nikolai.", self.station.train_has_arrived("Nikolai"))

    def test_adding_to_departure_when_we_check_and_see_our_train_is_in_arrivals(self):
        expected_departure = deque(["Toni", "Bobo"])
        expected_arrivals = deque([])

        self.assertEqual(f"Bobo is on the platform and will leave in 5 minutes.", self.station.train_has_arrived("Bobo"))

        self.assertEqual(expected_departure, self.station.departure_trains)
        self.assertEqual(expected_arrivals, self.station.arrival_trains)

    def test_popping_from_departure_trains_and_if_we_are_returning_true(self):
        expected_departure = deque([])

        self.assertTrue(self.station.train_has_left("Toni"))
        self.assertEqual(expected_departure, self.station.departure_trains)

    def test_the_false_return_after_having_no_trains(self):

        self.assertFalse(self.station.train_has_left("AHAHHAHA"))




if __name__ == "__main__":
    main()