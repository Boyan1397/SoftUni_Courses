size = int(input())
matrix = [list(input()) for _ in range(size)]

my_pos = []
total_amount = 0


for r in range(size):
    for c in range(size):
        if matrix[r][c] == "S":
            my_pos = [r, c]
            matrix[r][c] = "-"

directions ={"up": [-1, 0],
             "down": [1, 0],
             "right": [0, 1],
             "left": [0, -1],
}

whirlpool = False
command = input()
while command != "collect the nets":
    new_row = my_pos[0] + directions[command][0]
    new_col = my_pos[1] + directions[command][1]

    if new_row < 0:
        new_row = size - 1
    elif new_row >= size:
        new_row = 0
    if new_col < 0:
        new_col = size - 1
    elif new_col >= size:
        new_col = 0
    my_pos = [new_row, new_col]
    if matrix[new_row][new_col].isdigit():
        total_amount += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = "-"
    elif matrix[new_row][new_col] == "W":
        total_amount = 0
        last_coordinates = [new_row, new_col]
        whirlpool = True
        break

    command = input()

matrix[my_pos[0]][my_pos[1]] = "S"

if whirlpool:
    print(f"You fell into a whirlpool! "
          f"The ship sank and you lost the fish you caught. Last coordinates of the ship: [{','.join([str(el) for el in my_pos])}]")
else:
    if total_amount >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print("You didn't catch enough fish and didn't reach the quota! "
              f"You need {20 - total_amount} tons of fish more.")
    if total_amount > 0:
        print(f"Amount of fish caught: {total_amount} tons.")
    print(*[''.join(el) for el in matrix], sep="\n")



