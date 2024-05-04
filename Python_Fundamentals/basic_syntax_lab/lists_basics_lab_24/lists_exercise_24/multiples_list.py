starting_number = int(input())
count = int(input())
list_of_nums = []
for numbers in range(starting_number, (starting_number * count) + 1, starting_number):
    list_of_nums.append(numbers)
print(list_of_nums)