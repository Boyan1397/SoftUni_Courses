size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(size)]

command = input().split()
while command[0] != "END":
    row, col, value = int(command[1]), int(command[2]), int(command[3])
    if command[0] == "Add":
        if 0 <= row < size and 0 <= col < size:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        if 0 <= row < size and 0 <= col < size:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    command = input().split()

matrix = [print(*r) for r in matrix]