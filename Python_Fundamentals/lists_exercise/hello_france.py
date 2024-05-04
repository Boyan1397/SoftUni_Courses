ticket_cost = 150
items = input().split("|")
budget = int(input())
profit = 0
sell_prices = []
is_valid = False
for item in items:
    type,price = item.split("->")
    price = float(price)
    if type == "Clothes":
        if price <= 50.00:
            is_valid = True
        elif price >= 50:
            is_valid = False

    elif type == "Shoes":
        if price <= 35.00:
            is_valid = True
        elif price >= 35.00:
            is_valid = False
    elif type == "Accessories":
        if price <= 20.50:
            is_valid = True
        elif price >= 20.50:
            is_valid = False
    if is_valid:
        if budget >= price:
            budget -= price
            sell_price = price * 1.4
            profit += sell_price - price
            sell_prices.append(sell_price)


for sell_string in sell_prices:
    print(f"{sell_string:.2f}", end=" ")
print()


print(f"Profit: {profit:.2f}")
total_sum = budget + sum(sell_prices)
if total_sum >= ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")