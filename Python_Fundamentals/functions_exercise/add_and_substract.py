def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(result, third):
    return result - third


def add_and_subtract(first_num, second_num, third_num):
    sum_of_numbers = sum_numbers(first_num,second_num)
    final_result = subtract(sum_of_numbers, third_num)
    return final_result




first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))