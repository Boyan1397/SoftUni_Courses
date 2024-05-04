nums = [11,2,3,4,5,6]
print(sorted(nums))
#with lambda in descending order
sorted_nums = sorted(nums,key=lambda x:-x)
print(sorted_nums)
second_sorted = sorted(nums, reverse=True)
print(second_sorted)
#for strings
#names = input().split(", ")
#in ascending order
#sort_names = sorted(names,key=lambda x: len(x))
#print(sort_names)                                                  vajni neshta!
#in descening order and ascii ascending
#sorted_names = sorted(names, key=lambda x:(-len(x),x))
#print(sorted_names)
#map(example)
numbers_input = input().split()
multiplied = list(map(lambda x: int(x) * 2, numbers_input))
print(multiplied)
