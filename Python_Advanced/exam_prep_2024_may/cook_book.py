def cookbook(*args):
    for arg in args:
        print(arg[0])
        print(arg[1])
        print(arg[2])


print(cookbook(

("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),

("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),

("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),

("Croissant", "French", ["flour", "butter", "yeast"]),

("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))