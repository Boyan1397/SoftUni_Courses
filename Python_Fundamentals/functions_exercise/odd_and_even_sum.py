def odd_or_even(one_input):
    odd_sum_list = 0
    even_sum_list = 0
    for index in one_input:
        if int(index) % 2 == 0:
            even_sum_list += int(index)
        else:
            odd_sum_list += int(index)
    return odd_sum_list, even_sum_list


only_input = input()
odd_sums, even_sums = odd_or_even(only_input)
print(f"Odd sum = {odd_sums}, Even sum = {even_sums}")