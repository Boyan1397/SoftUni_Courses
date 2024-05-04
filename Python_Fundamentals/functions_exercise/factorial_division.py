def calculate_factorial(number):
    for current_num in range(1,number):
        number *= current_num
    return number


first_number = int(input())
second_number = int(input())
f_numb = calculate_factorial(first_number)
s_numb = calculate_factorial(second_number)
final_result = f_numb / s_numb
print(f"{final_result:.2f}")