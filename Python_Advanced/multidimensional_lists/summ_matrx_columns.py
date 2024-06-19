rows, columns = [int(el) for el in input().split(", ")]
matrix = [[int(el) for el in input().split()]for r in range(rows)]

for col in range(columns):
    total = 0
    for row in range(rows):
        total += matrix[row][col]
        print(matrix[row][col])
    print(total)
