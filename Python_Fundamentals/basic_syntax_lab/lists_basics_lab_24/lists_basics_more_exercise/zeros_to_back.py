current_input = [int(num) for num in input().split(", ")]
list_without_zeros = []
for el in current_input:
    if el != 0:
        list_without_zeros.append(el)
zeros = [0] * (len(current_input) - len(list_without_zeros))
final_list = list_without_zeros + zeros
print(final_list)