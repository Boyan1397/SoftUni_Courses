def orders(product, count):
    if product == "coffee":
        return count * 1.50
    elif product == "coke":
        return count * 1.40
    elif product == "water":
        return count * 1.00
    elif product == "snacks":
        return count * 2.00



name_of_product = input()
counter = int(input())

print(f"{orders(name_of_product, counter):.2f}")
