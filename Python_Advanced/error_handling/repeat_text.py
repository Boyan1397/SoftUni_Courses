my_word = input()
try:
    my_parameter = int(input())
    print(my_word*my_parameter)
except ValueError:
    print("Variable times must be an integer")