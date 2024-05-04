houses = [int(el) for el in input().split("@")]
current_index = 0
command = input()

while command != "Love!":
    length = int(command.split()[1])
    current_index += length
    if current_index not in range(len(houses)):
        current_index = 0
    if houses[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        houses[current_index] -= 2
        if houses[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {current_index}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    failed_ones = [s for s in houses if s != 0]
    print(f"Cupid has failed {len(failed_ones)} places.")



















