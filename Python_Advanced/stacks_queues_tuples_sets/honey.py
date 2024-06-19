from collections import deque
working_bees = deque(int(el) for el in input().split())
nectars = [int(el) for el in input().split()]
symbols = deque(input().split())

total_honey = 0
while working_bees and nectars:
    first_bee = working_bees.popleft()
    last_nectar = nectars.pop()
    if last_nectar >= first_bee:
        current_symbol = symbols.popleft()
        if current_symbol == "+":
            total_honey += abs(first_bee + last_nectar)
        elif current_symbol == "-":
            total_honey += abs(first_bee - last_nectar)
        elif current_symbol == "*":
            total_honey += abs(first_bee * last_nectar)
        elif current_symbol == "/":
            if last_nectar == 0:
                continue
            else:
                total_honey += abs(first_bee / last_nectar)
    else:
        working_bees.appendleft(first_bee)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(el) for el in working_bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(el) for el in nectars)}")