n_lines = int(input())
parking_set = set()
for _ in range(n_lines):
    data = input().split(", ")
    command, plate = data
    if command == "IN":
        parking_set.add(plate)
    elif command == "OUT":
        parking_set.discard(plate)

if not parking_set:
    print("Parking Lot is Empty")
else:
    print(*parking_set, sep="\n")