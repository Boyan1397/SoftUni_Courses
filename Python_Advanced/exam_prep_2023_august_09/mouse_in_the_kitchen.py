rows, cols = [int(el) for el in input().split(",")]

matrix = [list(input()) for _ in range(rows)]

mouse_pos = []
cheese_count = 0

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "M":
            matrix[r][c] = "*"
            mouse_pos = [r, c]
    cheese_count += matrix[r].count("C")

my_cheese = 0

directions ={"up": [-1, 0],
             "down": [1, 0],
             "right": [0, 1],
             "left": [0, -1],
}


while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break
    new_row = mouse_pos[0] + directions[command][0]
    new_col = mouse_pos[1] + directions[command][1]

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        print("No more cheese for tonight!")
        break
    if matrix[new_row][new_col] == "@":
        continue
    mouse_pos = [new_row, new_col]
    if matrix[new_row][new_col] == "C":
        my_cheese += 1
        matrix[new_row][new_col] = "*"
        if my_cheese == cheese_count:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[new_row][new_col] == "T":
        print("Mouse is trapped!")
        break

matrix[mouse_pos[0]][mouse_pos[1]] = "M"

for row in matrix:
    print(''.join(row))





