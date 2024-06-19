size = int(input())
matrix = [list(input()) for _ in range(size)]


removed_knights = 0
directions =(
    [2, 1], #down right
    [2, -1], #down left
    [-2, 1],#up right
    [-2, -1],#up left
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2],
)

while True:
    biggest_attacker = []
    max_sum = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "K":
                attacked = 0
                for direction in directions:
                    curr_row, curr_col = r + direction[0], c + direction[1]
                    if 0 <= curr_row < size and 0 <= curr_col < size:
                        if matrix[curr_row][curr_col] == "K":
                            attacked += 1
                if max_sum < attacked:
                    max_sum = attacked
                    biggest_attacker = [r, c]
    if biggest_attacker:
        matrix[biggest_attacker[0]][biggest_attacker[1]] = "0"
        removed_knights += 1

    if not biggest_attacker:
        break
print(removed_knights)




















