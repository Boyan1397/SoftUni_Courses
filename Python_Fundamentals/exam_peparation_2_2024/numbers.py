numbers_list = [int(s) for s in input().split()]
average = sum(numbers_list) / len(numbers_list)
filtered_nums = sorted(el for el in numbers_list if el > average)
MAXIMUM_NUMS = 5
if not filtered_nums:
    print("No")
else:
    for i in range(MAXIMUM_NUMS):
        if filtered_nums:
            print(filtered_nums.pop(), end=" ")
