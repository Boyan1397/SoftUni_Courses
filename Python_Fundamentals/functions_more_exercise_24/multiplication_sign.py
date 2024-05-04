def multiplication(first, second, third):
    lst = [first, second, third]
    counter = 0
    if first == 0 or second == 0 or third == 0:
        return "zero"
    if first > 0 and second > 0 and third > 0:
        return "positive"
    for el in lst:
        if el < 0:
            counter += 1
    if counter == 1 or counter == 3:
        return "negative"
    if counter == 2:
        return "positive"


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(multiplication(first_num, second_num, third_num))