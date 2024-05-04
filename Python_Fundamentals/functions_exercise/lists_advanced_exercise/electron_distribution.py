number_electrons = int(input())
shells = []
for shell in range(1, number_electrons +1):
    max_number = 2 * shell ** 2
    if number_electrons >= max_number:
        shells.append(max_number)
        number_electrons -= max_number
        if number_electrons == 0:
            break
    else:
        shells.append(number_electrons)
        break

print(shells)