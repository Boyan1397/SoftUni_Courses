first_list = input().split(", ")
second_list = input().split(", ")
new_list = []
for el in first_list:
    for element in second_list:
        if el in element:
            new_list.append(el)
            break
print(new_list)