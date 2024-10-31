from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Lora", "Cat", "meow")

    def test_if_the_innit_method_is_correct_and_check_the_get_kingdom_method(self):
        self.assertEqual("Lora", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_the_string_correctness_of_make_sound_method(self):
        expected_string = f"{self.mammal.name} makes {self.mammal.sound}"

        self.assertEqual(expected_string, self.mammal.make_sound())

    def test_the_get_kingdom_method_value(self):
        expected_value = "animals"

        self.assertEqual(expected_value, self.mammal.get_kingdom())

    def test_the_string_correctness_of_info_method(self):
        expected_string = f"{self.mammal.name} is of type {self.mammal.type}"

        self.assertEqual(expected_string, self.mammal.info())


if __name__ == "__main__":
    main()