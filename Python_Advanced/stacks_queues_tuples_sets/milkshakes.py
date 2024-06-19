from collections import deque

chocolates = deque(int(el) for el in input().split(", "))
cups_of_milk = deque(int(el) for el in input().split(", "))
milkshakes = 0

while chocolates and cups_of_milk:
    last_chocolate = chocolates[-1]
    first_milk = cups_of_milk.popleft()
    if last_chocolate <= 0 and first_milk <= 0:
        chocolates.pop()
        continue
    if last_chocolate <= 0:
        chocolates.pop()
        cups_of_milk.appendleft(first_milk)
        continue
    if first_milk <= 0:
        continue
    if last_chocolate == first_milk:
        chocolates.pop()
        milkshakes += 1
    elif last_chocolate != first_milk:
        cups_of_milk.append(first_milk)
        chocolates[-1] -= 5
    if milkshakes == 5:
        break

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(el) for el in chocolates)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(el) for el in cups_of_milk)}")
else:
    print("Milk: empty")