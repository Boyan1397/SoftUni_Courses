from collections import deque
size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(size)]

directions = (
    [-1, 0], #up
    [1, 0], #down
    [0, 1], #right
    [0, -1], #left
    [1, 1], #bottom-right
    [1, -1], #bottoom-left
    [-1, 1], #top-right
    [-1, -1], #top-left
    [0, 0], #self
)

bomb_coordinates = deque([[int(el) for el in els.split(",")] for els in input().split()])

for b_row, b_col in bomb_coordinates:
    if matrix[b_row][b_col] <= 0:
        continue
    for row_d, col_d in directions:
        current_row, current_col = b_row + row_d, b_col + col_d
        if 0 <= current_row < size and 0 <= current_col < size:
            if matrix[current_row][current_col] > 0:
                matrix[current_row][current_col] -= matrix[b_row][b_col]

alive_cells = [el for r in matrix for el in r if el > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
matrix = [print(*r) for r in matrix]
