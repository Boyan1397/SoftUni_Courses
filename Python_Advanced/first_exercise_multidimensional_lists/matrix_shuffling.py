def is_valid(vals_list):
    if len(vals_list) == 4:
        if (vals_list[0] in range(rows) and vals_list[1] in range(cols)
                and vals_list[2] in range(rows) and vals_list[-1] in range(cols)):
            return True
    return False


rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command_type, *values_list = [int(x) if x.isdigit() else x for x in input().split()]
    if command_type == "END":
        break
    if command_type == "swap":
        if is_valid(values_list):
            initial_row, initial_col, new_row, new_col = values_list
            matrix[initial_row][initial_col], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[initial_row][initial_col]
            for r in matrix:
                print(*r)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
