number_of_electrons = int(input())
shells_list = []
for shell in range(1, number_of_electrons + 1):
    maximum = 2 * shell ** 2
    if number_of_electrons > maximum:
        shells_list.append(maximum)
        number_of_electrons -= maximum
        if number_of_electrons == 0:
            break
    elif maximum > number_of_electrons:
        shells_list.append(number_of_electrons)
        break
print(shells_list)
