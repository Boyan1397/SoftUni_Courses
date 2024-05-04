def sum_all_evens_odds(string_number):
    even_sum = 0
    odd_sum = 0
    for el in string_number:
        current_number = int(el)
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number
    return odd_sum, even_sum


number_as_string = input()
odd_digits, even_digits = sum_all_evens_odds(number_as_string)
print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")
