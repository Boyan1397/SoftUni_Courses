
numbers = tuple(float(el) for el in input().split())
my_dict = {}
for number in numbers:
    if number not in my_dict.keys():
        my_dict[number] = 0
    my_dict[number] += 1

for key, value in my_dict.items():
    print(f"{key} - {value} times")