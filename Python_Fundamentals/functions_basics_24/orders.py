def my_orders(product,times):
    final_price = 0
    if product == "coffee":
        final_price = 1.50 * times
    elif product == "water":
        final_price = 1.00 * times
    elif product == "coke":
        final_price = 1.40 * times
    elif product == "snacks":
        final_price = 2.00 * times

    return (f"{final_price:.2f}")

type_product = input()
quantity = float(input())
print(my_orders(type_product, quantity))