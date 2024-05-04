def calculations(comment, first, second):
    result = 0
    if comment == "multiply":
        result = first * second
    elif comment == "divide":
        result = first // second
    elif comment == "add":
        result = first + second
    elif comment == "subtract":
        result = first - second

    return result

comment_input = input()
first_num = int(input())
second_num = int(input())
print(calculations(comment_input, first_num, second_num))