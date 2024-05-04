list_of_strings = input().split(", ")
count_of_beggars = int(input())
list_of_integers = [] #1 ,2 ,3 ,4 ,5

for number in list_of_strings:
    list_of_integers.append(int(number))

total_money =[]
start_index = 0
while start_index < count_of_beggars:
    current_sum = 0
    for index in range(start_index, len(list_of_integers),count_of_beggars):
        current_sum += list_of_integers[index]
    total_money.append(current_sum)
    start_index += 1
print(total_money)
