size = int(input())
matrix = [input().split() for _ in range(size)]

alice_position = []
found_tea = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "A":
            alice_position = [r, c]
            matrix[r][c] = "*"
            break

while found_tea < 10:
    command = input()
    row, col = alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]
    if not (0 <= row < size and 0 <= col < size):
        break
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    if matrix[row][col].isdigit():
        found_tea += int(matrix[row][col])

    alice_position = [row, col]
    matrix[row][col] = "*"

if found_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*el) for el in matrix]


