nums = ([int(element) for element in input().split(", ")])
even_number = ([index for index in range(len(nums)) if nums[index] % 2 == 0])
print(even_number)