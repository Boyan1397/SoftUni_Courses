items = input().split("|")
budget = int(input())
profit = 0
new_price_list = []
new_strings_list = []
for item in items:
    condition = False

    item_info = item.split("->")
    type_of_item = item_info[0]
    price = float(item_info[1])

    if type_of_item == "Clothes":
        if price <= 50.00:
            condition = True

    elif type_of_item == "Shoes":
        if price <= 35.00:
            condition = True

    elif type_of_item == "Accessories":
        if price <= 20.50:
            condition = True

    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            new_price = price + (price * 0.40)
            new_price_list.append(new_price)
            new_strings_list.append(f"{new_price:.2f}")

print(" ".join(new_strings_list))
print(f"Profit: {profit:.2f}")
total_price = budget + sum(new_price_list)
if total_price >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")