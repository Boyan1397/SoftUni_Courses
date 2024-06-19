rows = int(input())
matrix = []

for _ in range(rows):
    data = list(input())
    matrix.append(data)

searched_element = input()
is_found = False
for row_index in range(rows):
    for col_index in range(rows):
        if searched_element == matrix[row_index][col_index]:
            print(f"({row_index}, {col_index})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{searched_element} does not occur in the matrix")
