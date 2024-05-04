some_input = input().split()
my_dict = {}
while len(some_input) > 1:
    product_name, price, quantity = some_input[0], some_input[1], some_input[2]
    price = float(price)
    quantity = int(quantity)
    if product_name not in my_dict:
        my_dict[product_name] = []
        my_dict[product_name].append(quantity)
        my_dict[product_name].append(price)
    else:
        my_dict[product_name][0] += quantity
        my_dict[product_name][1] = price
    some_input = input().split()
for key, value in my_dict.items():
    total = value[0] * value[1]
    print(f"{key} -> {total:.2f}")