list_of_integers =[int(s) for s in input().split()] #list of integers
count_of_numbers_to_remove = int(input())

for number in range(count_of_numbers_to_remove):
    min_value = min(list_of_integers)
    list_of_integers.remove(min_value)
strings = ", ".join(str(num) for num in list_of_integers)
print(strings)