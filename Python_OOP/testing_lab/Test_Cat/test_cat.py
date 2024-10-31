from unittest import TestCase, main

from Python_OOP.testing_lab.Test_Cat.cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Lora")

    def test_is_innit_valid(self):
        expected_name = "Lora"

        self.assertEqual("Lora", expected_name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_the_exception_error_in_eat_method(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_are_fed_sleepy_setting_to_true_and_are_we_increasing_size_in_eat_method(self):
        expected_size = 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_the_exception_error_in_sleep_method(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_turning_the_sleepy_attr_to_false_if_fed_is_true(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()