nums_list = [int(el) for el in input().split(", ")]
indexes = [index for index in range(len(nums_list)) if nums_list[index] % 2 == 0]
print(indexes)