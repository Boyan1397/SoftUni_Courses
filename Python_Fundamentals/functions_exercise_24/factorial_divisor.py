def factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
first_result = factorial(first_number)
second_result = factorial(second_number)
total = first_result / second_result
print(f"{total:.2f}")