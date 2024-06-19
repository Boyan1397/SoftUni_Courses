collection = [
    [1, 2, 3],
    [4, 5, 6],
    [4, 8, 9]
]

collection[1][1] = 111
for row_index in range(len(collection)):
    for col_index in range(len(collection[row_index])):
        print(collection[row_index][col_index], end=" ")
    print()

# n = 3
# matrix = [] #[[0,0,0],[0,0,0],[0,0,0]]
# for row in range(3):
#     sub_list = []
#     for column in range(4):
#         sub_list.append(0)
#     matrix.append(sub_list)
# print(matrix)

# matrix = []
# for row in range(5):
#     matrix.append([])
#     for column in range(3):
#         matrix[row].append(0)
# print(matrix)

# matrix = []
# for i in range(3):
#     sub_list = []
#     for j in range(1,4):
#         sub_list.append(j)
#     matrix.append(sub_list)
# print(matrix)

# nest_matri = [[r for r in range(1,4)] for r in range(3)]
# print(nest_matri)
# bobo = []
# for sublist in nest_matri:
#     for el in sublist:
#         bobo.append(el)
# print(bobo)

# obob = [el for sublist in nest_matri for el in sublist]
# print(obob)