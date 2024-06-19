rows, cols = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for row in range(rows)]
square = []
max_sum = float("-inf")
for row in range(0,rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col+3]
        second_row = matrix[row +1][col:col+3]
        third_row = matrix[row+2][col:col+3]
        current_sum = (sum(first_row) + sum(second_row)+ sum(third_row))
        if max_sum < current_sum:
            square = [first_row, second_row, third_row]
            max_sum = current_sum
print(f"Sum = {max_sum}")
square = [print(*r) for r in square]