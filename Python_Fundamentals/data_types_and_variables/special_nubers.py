number = int(input())
for current_num in range(1,number +1):
    sums_count = 0
    current_num_as_string = str(current_num)
    for digit in current_num_as_string:
        sums_count += int(digit)
    is_special = False
    if sums_count == 5 or sums_count == 7 or sums_count == 11:
        is_special = True
    print(f"{current_num} -> {is_special}")
