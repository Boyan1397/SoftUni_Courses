class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients


    @classmethod
    def pepperoni(cls):
        return cls(["tomatoes", "salami", "cheese"])


    @classmethod
    def quattro(cls, additional=[]):
        all_ingredients = ["cheese", "smelly_cheese", "mortadella"] + additional #extending the main ingredients
        return cls(all_ingredients)

    def add_ing(self, ingredient):
        self.ingredients.append(ingredient)


# my_pizza = Pizza(["banana", "pineapple", "testo"])
# print(my_pizza.ingredients)
# p_pizza = Pizza.pepperoni()
# p_pizza.add_ing("onions")
# print(p_pizza.ingredients)

quattro = Pizza.quattro(["panikola"])
print(quattro.ingredients)

