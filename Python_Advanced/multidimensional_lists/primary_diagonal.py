rows = int(input())
matrix = []

for _ in range(rows):
    sublist = [int(el) for el in input().split()]
    matrix.append(sublist)

sum_of_diagonal = 0
for row in range(rows):
    sum_of_diagonal += matrix[row][row]
print(sum_of_diagonal)