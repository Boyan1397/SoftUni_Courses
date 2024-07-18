from collections import deque

size = int(input())
commands = deque(input().split(", "))
matrix = [list(input()) for _ in range(size)]
squirrel_pos = []
hazelnuts = 0

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "s":
            squirrel_pos = [r, c]
            matrix[r][c] = "*"
            break

directions ={"up": [-1, 0],
             "down": [1, 0],
             "right": [0, 1],
             "left": [0, -1],
}

die = False
while commands:
    direction = commands.popleft()
    new_row = squirrel_pos[0] + directions[direction][0]
    new_col = squirrel_pos[1] + directions[direction][1]
    if not (0 <= new_row < size and 0 <= new_col < size):
        print("The squirrel is out of the field.")
        die = True
        break
    squirrel_pos = [new_row, new_col]

    if matrix[new_row][new_col] == "h":
        hazelnuts += 1
        matrix[new_row][new_col] = "*"
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    elif matrix[new_row][new_col] == "t":
        die = True
        print("Unfortunately, the squirrel stepped on a trap...")
        break


if not die and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")












