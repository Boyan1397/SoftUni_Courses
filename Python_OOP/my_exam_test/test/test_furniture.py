from unittest import TestCase, main

from project.furniture import Furniture


class TestFurniture(TestCase):
    def setUp(self):
        self.furniture = Furniture("Chair", 50.0, (120, 60, 90))

    def test_correct_innit(self):
        self.assertEqual("Chair", self.furniture.model)
        self.assertEqual(50.0, self.furniture.price)
        self.assertEqual((120, 60, 90), self.furniture.dimensions)
        self.assertTrue(self.furniture.in_stock)
        self.assertIsNone(self.furniture.weight)

    def test_model_setter_error_if_nothing(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = ""

        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ve.exception))

    def test_model_setter_error_if_more_than_50(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = "asdfsaddsdgsdfsadfasdfsadfsdfsadfasdffasdfasdfsadfasfasdfasdfsadfsadfsadfasd"

        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ve.exception))

    def test_price_error_if_its_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.price = -1

        self.assertEqual("Price must be a non-negative number.", str(ve.exception))

    def test_dimension_error_if_len_iss_diff_than_three(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1, 3)

        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ve.exception))

    def test_dimensions_error_when_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (150, -75, 100)

        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ve.exception))

    def test_weight_error_when_is_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.weight = -1

        self.assertEqual("Weight must be greater than zero.",  str(ve.exception))

    def test_weight_error_when_is_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.weight = 0

        self.assertEqual("Weight must be greater than zero.", str(ve.exception))

    def test_get_available_status_str_return_when_is_in_stock(self):
        self.furniture.in_stock = True
        self.assertEqual(self.furniture.get_available_status(), "Model: Chair is currently in stock.")

    def test_get_available_status_str_return_when_is_not_in_stock(self):
        self.furniture.in_stock = False
        self.assertEqual(self.furniture.get_available_status(), "Model: Chair is currently unavailable.")

    def test_get_specifications(self):
        self.furniture.weight = 20.0
        expected = "Model: Chair has the following dimensions: 120mm x 60mm x 90mm and weighs: 20.0"
        self.assertEqual(self.furniture.get_specifications(), expected)

        self.furniture.weight = None
        expected = "Model: Chair has the following dimensions: 120mm x 60mm x 90mm and weighs: N/A"
        self.assertEqual(self.furniture.get_specifications(), expected)

if __name__ == "__main__":
    main()