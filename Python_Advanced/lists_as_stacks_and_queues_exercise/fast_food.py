from collections import deque

quantity = int(input())
orders = deque([int(el) for el in input().split()])

print(max(orders))

while orders:
    order = orders.popleft()
    if quantity >= order:
        quantity -= order
    else:
        orders.appendleft(order)
        print(f"Orders left:", *orders)
        break
if not orders:
    print("Orders complete")