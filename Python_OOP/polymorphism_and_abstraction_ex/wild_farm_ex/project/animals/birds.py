from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        food_quantity = 0.25 * food.quantity
        self.weight += food_quantity
        self.food_eaten += food.quantity


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        food_quantity = 0.35 * food.quantity
        self.weight += food_quantity
        self.food_eaten += food.quantity