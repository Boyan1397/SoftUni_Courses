#print(*[1,2234,53,62],sep= "__")
#numbers = [1, 2, 3, 6, 4, 0, -1, 5]
#number = [number * 3 for number in numbers if number > 0]
           #output ,   variable              parameter

#print(number)

#print([number for number in range(6 + 1)])
#print([nums**2 for nums in range(1,5 + 1)])
#nums = [1,2,3,4,5,6]
#print([numbers**2 for numbers in nums])
#numbers = [1,2,3,4,5,6]
#print([el for el in numbers if el % 2 == 0])

#numbers = [int(element) for element in input().split(", ")]
#print([index for index in range(len(numbers)) if numbers[index] % 2 == 0])

#nums = [int(element) for element in input().split(", ")] #=== string list into numbers list
#print([index for index in range(len(nums)) if nums[index] %2 == 0]) #=== index comperhansion

#if-else
#nums = [1,2,3,4,5,6]
#print(["even" if element % 2 == 0 else "odd" for element in nums])
           #if                      else           loop
#map
nums = ["1", "2", "3", "4", "5"]
print([int(el) for el in nums])
print(list(map(int, nums)))