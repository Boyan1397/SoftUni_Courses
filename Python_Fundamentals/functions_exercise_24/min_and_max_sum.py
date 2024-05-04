def min_max_sum(strings_list):
    number_list = []
    for el in strings_list:
        current_number = int(el)
        number_list.append(current_number)

    min_number = min(number_list)
    max_number = max(number_list)
    sums_numbers = sum(number_list)
    return min_number, max_number, sums_numbers


list_of_strings = input().split()
minimal_number, maximum_number, sum_numbers = min_max_sum(list_of_strings)
print(f"The minimum number is {minimal_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_numbers}")