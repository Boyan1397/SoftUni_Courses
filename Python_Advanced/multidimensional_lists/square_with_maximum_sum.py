rows, columns = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(rows):
    data_sublist = [int(el) for el in input().split(", ")]
    matrix.append(data_sublist)

submatrix = []
max_number = float('-inf')

for row_index in range(rows-1):
    for col_index in range(columns-1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index+1]
        below_element = matrix[row_index+1][col_index]
        diagonal_element = matrix[row_index+1][col_index+1]

        current_sum = (current_element + next_element + below_element + diagonal_element)
        if current_sum > max_number:
            max_number = current_sum
            submatrix = [[current_element, next_element],[below_element, diagonal_element]]

print(*submatrix[0])
print(*submatrix[1])
print(max_number)

