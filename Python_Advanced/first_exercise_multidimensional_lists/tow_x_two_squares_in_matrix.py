rows, columns = [int(el) for el in input().split()]

matrix = [input().split() for _ in range(rows)]

count_of_identical_fours = 0
for row in range(rows-1):
    for col in range(columns-1):
        current_element = matrix[row][col]
        next_element = matrix[row][col+1]
        below_element = matrix[row+1][col]
        diagonal_element = matrix[row+1][col+1]
        if current_element == next_element == below_element == diagonal_element:
            count_of_identical_fours += 1

print(count_of_identical_fours)