def my_string(name):
    return lambda num: num * name

string_input = input()
number_input = int(input())

my_func = my_string(string_input)
print(my_func(number_input))
###########################
result = lambda a, b: a * b

name = input()
num = int(input())
print(result(name, num))