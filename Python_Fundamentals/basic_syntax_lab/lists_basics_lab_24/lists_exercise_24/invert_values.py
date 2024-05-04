current_list = input().split()
filtered_list = []
for number in current_list:
    opposite_number = int(number) * (-1)
    filtered_list.append(opposite_number)
print(filtered_list)