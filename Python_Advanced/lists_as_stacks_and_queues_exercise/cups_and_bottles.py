from collections import deque

# 4 2 10 5 cups >
# 3 15 15 11 6 bottles <

cups_and_capacities = deque(int(el) for el in input().split())
bottles_and_capacities = deque(int(el) for el in input().split())
wasted_water = 0

while True:

    if not cups_and_capacities:
        print(f"Bottles: {' '.join(str(el) for el in bottles_and_capacities)}")
        break

    if not bottles_and_capacities:
        print(f"Cups: {' '.join(str(el )for el in cups_and_capacities)}")
        break
    current_cup = cups_and_capacities.popleft()
    current_bottle = bottles_and_capacities.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    elif current_bottle < current_cup:
        cups_and_capacities.appendleft(current_cup)
        cups_and_capacities[0] -= current_bottle

print(f"Wasted litters of water: {wasted_water}")