rows, cols = [int(el) for el in input().split()]

matrix = [list(input()) for _ in range(rows)]

boy_pos = []

is_collected = False
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "B":
            boy_pos = [r, c]
            break
starting_pos =[boy_pos[0], boy_pos[1]]

directions ={"up": [-1, 0],
             "down": [1, 0],
             "right": [0, 1],
             "left": [0, -1],
}

is_collected = False

while True:
    direction = input()
    new_row = boy_pos[0] + directions[direction][0]
    new_col = boy_pos[1] + directions[direction][1]

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        print("The delivery is late. Order is canceled.")
        matrix[starting_pos[0]][starting_pos[1]] = " "
        break
    if matrix[new_row][new_col] == "*":
        continue
    boy_pos = [new_row, new_col]
    if matrix[new_row][new_col] == "-":
        matrix[new_row][new_col] = "."

    elif matrix[new_row][new_col] == "P":
        is_collected = True
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[new_row][new_col] = "R"
        continue
    elif is_collected:
        if matrix[new_row][new_col] == "A":
            print("Pizza is delivered on time! Next order...")
            matrix[new_row][new_col] = "P"
            break

print(*[''.join(el) for el in matrix], sep="\n")








