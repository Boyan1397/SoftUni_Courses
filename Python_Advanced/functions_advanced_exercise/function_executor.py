def func_executor(*data):
    final = []
    for func, args in data:
        final.append(f"{func.__name__} - {func(*args)}")
    return "\n".join(final)


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))