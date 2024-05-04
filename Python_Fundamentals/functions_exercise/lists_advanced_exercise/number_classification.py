numbers = input().split(", ")
def positive_numbers(numbers):
    return ", ".join(num for num in numbers if int(num) >= 0)

def negative_numbers(numbers):
    return ", ".join(num for num in numbers if int(num) < 0)

def even_numbers(numbers):
    return ", ".join(num for num in numbers if int(num) % 2 == 0)

def odd_numbers(numbers):
    return ", ".join(num for num in numbers if int(num) % 2 != 0)

print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")




