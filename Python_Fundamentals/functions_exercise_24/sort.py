def sorts(list_of_strings):
    list_numbers = []
    for el in list_of_strings:
        current_num = int(el)
        list_numbers.append(current_num)
    return sorted(list_numbers)


strings_list = input().split()
print(sorts(strings_list))