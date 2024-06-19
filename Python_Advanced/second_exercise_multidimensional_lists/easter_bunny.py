size = int(input())
matrix = [input().split() for _ in range(size)]
bunny_position = []
maximum_eggs = float("-inf")
biggest_eggs_positions = []
final_direction = None
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "B":
            bunny_position = [r, c]
            break

for direction, positions in directions.items():
    row, col = bunny_position[0] + positions[0], bunny_position[1] + positions[1]
    current_eggs_count = 0
    current_position = []
    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break
        if matrix[row][col].isdigit():
            current_eggs_count += int(matrix[row][col])
            current_position.append([row, col])
        row += positions[0]
        col += positions[1]

    if maximum_eggs <= current_eggs_count:
        maximum_eggs = current_eggs_count
        biggest_eggs_positions = current_position
        final_direction = direction
print(final_direction)
[print(el) for el in biggest_eggs_positions]
print(maximum_eggs)




