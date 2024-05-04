factor = int(input())
count = int(input())
list_of_nums = []
for num in range(factor,factor * count +1, factor):
    list_of_nums.append(num)

print(list_of_nums)