rows, columns = [int(el) for el in input().split(", ")]
total = 0
matrix = []
for row in range(rows):
    element = [int(el) for el in input().split(", ")]
    total += sum(element)
    matrix.append(element)
print(total)
print(matrix)

# rows, columns = [int(el) for el in input().split(", ")]
# total = 0
# matrix = []
# for row in range(rows):
#     sublist = []
#     data = [int(el) for el in input().split(", ")]
#     for col in range(columns):
#         current_element = data[col]
#         total += current_element
#         sublist.append(current_element)
#     matrix.append(sublist)
# print(matrix)