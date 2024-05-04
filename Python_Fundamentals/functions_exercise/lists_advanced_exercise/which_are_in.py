first_line = input().split(", ")
second_line = input().split(", ")
last_list = []
for element in first_line:
    for el in second_line:
        if element in el:
            last_list.append(element)
            break
print(last_list)

