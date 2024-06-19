def move_command(direction, steps_count):
    row = my_position[0] + (directions[direction][0] * steps_count)
    col = my_position[1] + (directions[direction][1] * steps_count)
    if not (0 <= row < size and 0 <= col < size):
        return my_position
    if matrix[row][col] == "x":
        return my_position
    return [row, col]


def shoot_command(direction):
    row = my_position[0] + directions[direction][0]
    col = my_position[1] + directions[direction][1]
    while True:
        if not (0 <= row < size and 0 <= col < size):
            return None
        if matrix[row][col] == "x":
            matrix[row][col] = "."
            return [row, col]
        row += directions[direction][0]
        col += directions[direction][1]


size = 5
matrix = [input().split() for _ in range(size)]

my_position = []
all_targets_count = 0
count_of_shot = 0
current_shot_target = []
shot_targets = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "A":
            my_position = [r, c]
    all_targets_count += matrix[r].count("x")

for _ in range(int(input())):
    command = input().split()
    if command[0] == "move":
        my_position = move_command(command[1], int(command[2]))
    elif command[0] == "shoot":
        current_shot_target = shoot_command(command[1])
        if current_shot_target:
            shot_targets.append(current_shot_target)
            count_of_shot += 1
            if count_of_shot == all_targets_count:
                print(f"Training completed! All {count_of_shot} targets hit.")
                break

if count_of_shot < all_targets_count:
    print(f"Training not completed! {all_targets_count - count_of_shot} targets left.")
[print(el) for el in shot_targets]



