from collections import deque
size = int(input())
commands = deque(input().split())
possible_directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}
matrix = [input().split() for _ in range(size)]

miner_pos = []
my_coal = 0
total_coal = 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "s":
            matrix[r][c] = "*"
            miner_pos = [r, c]

for r in range(size):
    total_coal += matrix[r].count("c")

while commands:

    command = commands.popleft()
    current_row, current_col = miner_pos[0] + possible_directions[command][0], miner_pos[1] + possible_directions[command][1]
    if not (0 <= current_row < size and 0 <= current_col < size):
        continue
    miner_pos = [current_row, current_col]
    if matrix[current_row][current_col] == "c":
        my_coal += 1
        matrix[current_row][current_col] = "*"
        if my_coal == total_coal:
            print(f"You collected all coal! ({current_row}, {current_col})")
            break
    elif matrix[current_row][current_col] == "e":
        print(f"Game over! ({current_row}, {current_col})")
        break
else:
    print(f"{total_coal - my_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")




