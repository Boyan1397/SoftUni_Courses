presents = int(input())
size = int(input())
matrix = [input().split() for _ in range(size)]
santa_position = []

total_nice_kids = 0
count_nice_kids = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "S":
            santa_position = [r, c]
            matrix[r][c] = "-"
    total_nice_kids += matrix[r].count("V")

while True:
    if presents <= 0:
        break
    command = input()
    if command == "Christmas morning":
        break
    row, col = santa_position[0] + directions[command][0], santa_position[1] + directions[command][1]

    if matrix[row][col] == "V":
        presents -= 1
        count_nice_kids += 1
    elif matrix[row][col] == "X":
        presents -= 1
    elif matrix[row][col] == "C":
        for direction in directions.keys():
            if presents <= 0:
                break
            c_row, c_col = row + directions[direction][0], col + directions[direction][1]
            if matrix[c_row][c_col] == "V":
                presents -= 1
                count_nice_kids += 1
            elif matrix[c_row][c_col] == "X":
                presents -= 1
            matrix[c_row][c_col] = "-"

    santa_position = [row, col]
    matrix[row][col] = "-"

if presents <= 0:
    if total_nice_kids > count_nice_kids:
        print("Santa ran out of presents!")

matrix[santa_position[0]][santa_position[1]] = "S"
[print(*el) for el in matrix]

if total_nice_kids == count_nice_kids :
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
elif total_nice_kids > count_nice_kids:
    print(f"No presents for {total_nice_kids - count_nice_kids} nice kid/s.")
