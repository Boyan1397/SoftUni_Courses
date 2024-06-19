def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key= lambda kvp: (-len(kvp[1]), kvp[0])) #сортирай по броя но ако има съвпадение и в азбучен ред
    final = ""
    for cheese_name, value in sorted_cheeses:
        final += cheese_name + "\n"
        for el in (sorted(value, reverse=True)):
            final += f"{el}\n"
    return final

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

