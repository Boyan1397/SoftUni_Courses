my_string = input()
for index in range(len(my_string)):
    if my_string[index] == ":":
        print(my_string[index] + my_string[index+1])