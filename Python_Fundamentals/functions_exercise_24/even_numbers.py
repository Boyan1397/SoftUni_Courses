def evens(list_of_strings):
    evens_list = []
    for el in list_of_strings:
        current_num = int(el)
        if current_num % 2 == 0:
            evens_list.append(current_num)
    return evens_list

numbers_list = input().split()
print(evens(numbers_list))

