rows_and_cols = int(input())
matrix = [list(input()) for _ in range(rows_and_cols)]

my_energy = 15

bee_position = []
for r in range(rows_and_cols):
    for c in range(rows_and_cols):
        if matrix[r][c] == "B":
            bee_position = [r, c]
            matrix[r][c] = "-"
            break

my_directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1],
}

total_nectar = 0
restored = False

while True:
    some_direction = input()
    new_row = bee_position[0] + my_directions[some_direction][0]
    new_col = bee_position[1] + my_directions[some_direction][1]
    if 0 > new_row:
        new_row = rows_and_cols - 1
    elif new_row >= rows_and_cols:
        new_row = 0
    if 0 > new_col:
        new_col = rows_and_cols - 1
    elif new_col >= rows_and_cols:
        new_col = 0
    bee_position = [new_row, new_col]
    my_energy -= 1

    if matrix[new_row][new_col].isdigit():
        total_nectar += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = "-"
    elif matrix[new_row][new_col] == "H":
        if total_nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {my_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if my_energy <= 0:
        if total_nectar >= 30 and not restored:
            my_energy += (total_nectar - 30)
            total_nectar = 30
            restored = True
        else:
            print("This is the end! Beesy ran out of energy.")
            break

matrix[bee_position[0]][bee_position[1]] = "B"

for row in matrix:
    print(''.join(row))
