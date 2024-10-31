from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Lora1104", 7, 100.5, 50.5)
        self.enemy = Hero("Boyan1397", 10, 200, 70)

    def test_innit_method_attr_correctness(self):
        self.assertEqual("Lora1104", self.hero.username)
        self.assertEqual(7, self.hero.level)
        self.assertEqual(100.5, self.hero.health)
        self.assertEqual(50.5, self.hero.damage)

    def test_exception_error_when_enemy_and_hero_have_same_names(self):
        self.enemy.username = "Lora1104"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_value_error_when_hero_health_is_below_or_equal_to_zero(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_value_error_when_enemy_health_is_below_or_equal_to_zero(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_if_both_players_health_is_below_or_equal_to_zero_after_damage(self):

        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_if_enemy_health_is_below_or_equal_to_zero_after_damage(self):
        self.hero.health = 10000


        self.assertEqual("You win", self.hero.battle(self.enemy))

    def test_the_additional_values_to_the_hero_when_enemy_has_no_health(self):
        self.hero.health = 10000
        self.enemy.damage = 400

        expected_level = self.hero.level + 1
        expected_health = self.hero.health - 4000 + 5
        expected_damage = self.hero.damage + 5

        self.hero.battle(self.enemy)

        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_if_hero_health_is_below_or_equal_to_zero_after_damage(self):
        self.enemy.health = 10000

        self.assertEqual("You lose", self.hero.battle(self.enemy))

    def test_the_additional_values_to_the_enemy_when_hero_has_no_health(self):
        self.enemy.health = 10000
        self.hero.damage = 400

        expected_level = self.enemy.level + 1
        expected_health = self.enemy.health - 2800 + 5
        expected_damage = self.enemy.damage + 5

        self.hero.battle(self.enemy)

        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_the_str_method_result_is_the_same(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_result, self.hero.__str__())


if __name__ == "__main__":
    main()
