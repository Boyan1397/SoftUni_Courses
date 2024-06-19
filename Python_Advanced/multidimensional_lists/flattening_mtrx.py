rows = int(input())
matrix = []
for row in range(rows):
    sublist = [int(el) for el in input().split(", ")]
    matrix.extend(sublist)
print(matrix)


# rows = int(input())
# matrix = []
# for row in range(rows):
#     sublist = input().split(", ")
#     for el in sublist:
#         matrix.append(int(el))
# print(matrix)

# rows = int(input())
# matrix = []
# for row in range(rows):
#     sublist = input().split(", ")
#     matrix.append(sublist)
#
# flattened = [int(el) for sublist in matrix for el in sublist]
# print(flattened)

