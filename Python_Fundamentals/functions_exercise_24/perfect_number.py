def is_perfect_num(num_input):
    numbers_sum = 0
    for num in range(1, num_input):
        if num_input % num == 0:
            numbers_sum += num
    if numbers_sum == num_input:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect_num(number))