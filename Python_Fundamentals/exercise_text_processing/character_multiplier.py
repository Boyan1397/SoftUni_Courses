first, second = input().split()
total_sum = 0
if len(first) > len(second):
    for index in range(len(second)):
        total_sum += (ord(first[index]) * ord(second[index]))
    for element_to_add in range(len(second), len(first)):
        total_sum += ord(first[element_to_add])
elif len(second) > len(first):
    for index in range(len(first)):
        total_sum += (ord(first[index]) * ord(second[index]))
    for element_to_add in range(len(first), len(second)):
        total_sum += ord(second[element_to_add])
elif len(first) == len(second):
    for index in range(len(second)):
        total_sum += (ord(first[index]) * ord(second[index]))
print(total_sum)