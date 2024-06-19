numbers_list = [int(el) for el in input().split(", ")] #cant split integer type error maybe
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]  #out of range
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result) # name error