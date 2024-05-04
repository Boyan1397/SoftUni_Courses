def add_and_subtract(first, second, third):
    total_result = (first + second) - third
    return total_result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


first_num = int(input())
second_num = int(input())
third_num = int(input())
first_sum = sum_numbers(first_num, second_num)
print(subtract(first_sum, third_num))