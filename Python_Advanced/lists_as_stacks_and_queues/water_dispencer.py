from collections import deque
quantity = int(input())
command_name = input()
queue = deque()
while command_name != "Start":
    queue.append(command_name)
    command_name = input()

command_name = input()
while command_name != "End":
    if command_name.isdigit():
        litters = int(command_name)
        if quantity - litters >= 0:
            quantity -= litters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    elif "refill" in command_name:
        refill_liters = int(command_name.split()[1])
        quantity += refill_liters
    command_name = input()

print(f"{quantity} liters left")