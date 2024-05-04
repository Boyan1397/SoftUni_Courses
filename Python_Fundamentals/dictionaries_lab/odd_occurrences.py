list_of_items = input().lower().split()
some_dict = {}
for element in list_of_items:
    if element not in some_dict:
        some_dict[element] = 0
        some_dict[element] += 1
    else:
        some_dict[element] += 1
for key, value in some_dict.items():
    if value % 2 != 0:
        print(key, end=" ")