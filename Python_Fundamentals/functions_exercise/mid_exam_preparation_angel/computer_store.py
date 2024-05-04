command = input()
net_price = 0

while command != "special" and command != "regular":
    price = float(command)
    if price > 0:
        net_price += price
        