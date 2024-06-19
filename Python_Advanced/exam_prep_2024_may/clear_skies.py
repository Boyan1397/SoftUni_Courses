size = int(input())
matrix = [list(input()) for _ in range(size)]

initial_armor = 300
count_of_enemies = 0

jet_pos = []

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "J":
            jet_pos = [r, c]
            matrix[r][c] = "-"
    count_of_enemies += matrix[r].count("E")


directions ={"up": [-1, 0],
             "down": [1, 0],
             "right": [0, 1],
             "left": [0, -1],
}

while initial_armor:
    direction = input()

    new_row = jet_pos[0] + directions[direction][0]
    new_col = jet_pos[1] + directions[direction][1]
    jet_pos = [new_row, new_col]
    if matrix[new_row][new_col] == "E":
        matrix[new_row][new_col] = "-"
        count_of_enemies -= 1
        if count_of_enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            matrix[new_row][new_col] = "J"
            print('\n'.join([''.join(el) for el in matrix]))

            break
        elif count_of_enemies > 0:
            initial_armor -= 100
            if initial_armor <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!")
                matrix[new_row][new_col] = "J"
                print('\n'.join([''.join(el) for el in matrix]))
                break
    elif matrix[new_row][new_col] == "R":
        initial_armor = 300
        matrix[new_row][new_col] = "-"

