numbers = input().split()
list_absolute = []

for number in numbers:
    list_absolute.append(abs(float(number)))
print(list_absolute)