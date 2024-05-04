string_of_beggars = input().split(", ")
count_beggars = int(input())

integer_of_beggars = []
for beggar in string_of_beggars:
    int_beggar = int(beggar)
    integer_of_beggars.append(int_beggar)
total_sum_for_each_beggars = []
start_index = 0
while start_index < count_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(integer_of_beggars), count_beggars):
        current_beggar_sum += integer_of_beggars[current_index]
    total_sum_for_each_beggars.append(current_beggar_sum)
