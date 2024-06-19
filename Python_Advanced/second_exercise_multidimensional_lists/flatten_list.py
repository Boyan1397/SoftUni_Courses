matrix = input().split("|")
matrix.reverse()
matrix = [int(el) for els in matrix for el in els.split()]
print(*matrix)