from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        food_quantity = 0.10 * food.quantity
        self.weight += food_quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        food_quantity = 0.40 * food.quantity
        self.weight += food_quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        food_quantity = 0.30 * food.quantity
        self.weight += food_quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        food_quantity = 1.00 * food.quantity
        self.weight += food_quantity
        self.food_eaten += food.quantity
