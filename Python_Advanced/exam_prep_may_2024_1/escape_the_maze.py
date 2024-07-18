size = int(input())
matrix = [list(input()) for _ in range(size)]

traveller_pos = []

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "P":
            traveller_pos = [r, c]
            matrix[r][c] = "-"
            break

directions ={"up": [-1, 0],
             "down": [1, 0],
             "right": [0, 1],
             "left": [0, -1],
}

health = 100
while True:
    direction = input()

    new_row = traveller_pos[0] + directions[direction][0]
    new_col = traveller_pos[1] + directions[direction][1]

    if not (0 <= new_row < size and 0 <= new_col < size):
        continue
    traveller_pos = [new_row, new_col]

    if matrix[new_row][new_col] == "M":
        health -= 40
        if health <= 0:
            health = 0
            break
        else:
            matrix[new_row][new_col] = "-"

    elif matrix[new_row][new_col] == "H":
        health += 15
        if health >= 100:
            health = 100
        matrix[new_row][new_col] = "-"

    elif matrix[new_row][new_col] == "X":
        break

matrix[traveller_pos[0]][traveller_pos[1]] = "P"

if health <= 0:
    print("Player is dead. Maze over!")
else:
    print("Player escaped the maze. Danger passed!")

print(f"Player's health: {health} units")
print(*[''.join(el) for el in matrix], sep= "\n")