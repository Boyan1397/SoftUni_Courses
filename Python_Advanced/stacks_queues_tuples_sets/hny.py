from collections import deque
working_bees = deque(int(el) for el in input().split())
nectars = [int(el) for el in input().split()]
symbols = deque(input().split())
total_honey = 0
functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}
while working_bees and nectars:
    first_bee = working_bees.popleft()
    last_nectar = nectars.pop()
    if last_nectar < first_bee:
        working_bees.appendleft(first_bee)
    else:
        total_honey += abs(functions[symbols.popleft()](first_bee, last_nectar))

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(el) for el in working_bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(el) for el in nectars)}")