from unittest import TestCase, main

from Python_OOP.testing_lab.Test_List.ex_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.i_list = IntegerList(3.4, 1, 2, 3, 4, "Nikola")

    def test_check_the_for_loop_taking_only_integers_in_the_innit_method(self):
        expected_list = [1, 2, 3, 4]

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_check_value_error_because_not_integer_in_add_method(self):
        element = 5.5
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(element)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_check_appending_the_data_into_the_list_in_add_method(self):
        expected_list = self.i_list.get_data() + [3]

        self.assertEqual(expected_list, self.i_list.add(3))

    def test_the_index_error_raising_because_index_out_of_range_in_insert_method(self):

        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(1000, 2)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_value_error_because_not_integer_in_insert_method_element(self):

        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(1, 4.543)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_inserting_in_the_insert_method(self):
        expected_insert = self.i_list.get_data().copy()
        expected_insert = expected_insert.insert(1, 40)

        self.assertEqual(expected_insert, self.i_list.insert(1, 40))

    def test_getting_the_biggest_integer_from_get_biggest_method(self):
        self.assertEqual(4, self.i_list.get_biggest())

    def test_getting_the_element_by_the_index(self):
        self.assertEqual(1, self.i_list.get_index(2))




if __name__ == "__main__":
    main()