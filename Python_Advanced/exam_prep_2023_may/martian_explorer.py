from collections import deque
size = 6

matrix = [input().split() for r in range(size)]
rover_pos = []

found_deposits = {
    'Water': 0,
    'Metal': 0,
    'Concrete': 0
}

directions ={"up": [-1, 0],
             "down": [1, 0],
             "right": [0, 1],
             "left": [0, -1],
}

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "E":
            rover_pos = [r, c]

commands = deque(input().split(", "))
while commands:
    direction = commands.popleft()
    r, c = directions[direction][0], directions[direction][1]
    new_row = rover_pos[0] + r
    new_col = rover_pos[1] + c
    if 0 > new_row:
        new_row = size - 1
    elif new_row >= size:
        new_row = 0
    if 0 > new_col:
        new_col = size - 1
    elif new_col >= size:
         new_col = 0
    rover_pos = [new_row, new_col]

    if matrix[new_row][new_col] == "W":
        found_deposits["Water"] += 1
        print(f"Water deposit found at ({new_row}, {new_col})")
    elif matrix[new_row][new_col] == "M":
        found_deposits["Metal"] += 1
        print(f"Metal deposit found at ({new_row}, {new_col})")
    elif matrix[new_row][new_col] == "C":
        found_deposits["Concrete"] += 1
        print(f"Concrete deposit found at ({new_row}, {new_col})")
    elif matrix[new_row][new_col] == "R":
        print(f"Rover got broken at ({new_row}, {new_col})")
        break

if all(value > 0 for value in found_deposits.values()):
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")

















