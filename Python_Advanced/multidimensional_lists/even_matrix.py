rows = int(input())
matrix = []

for row in range(rows):
    sublist = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(sublist)
print(matrix)

# rows = int(input())
# matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for row in range(rows)]
# print(matrix)