rows = int(input())
matrix = []
#[[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
for _ in range(rows):
    data = [int (el) for el in input().split()]
    matrix.append(data)

p = 0
s = 0
for row_index in range(rows):
    p += matrix[row_index][row_index]
    s += matrix[row_index][rows - row_index - 1]

print(p)
print(s)
