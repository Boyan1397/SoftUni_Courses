my_strings = input().split()
total_sum = 0
for some_string in my_strings:
    first_letter = some_string[0]
    last_letter = some_string[-1]
    number = int(some_string[1:-1])
    if first_letter.isupper():
        total_sum += number / (ord(first_letter) - 64)
    elif first_letter.islower():
        total_sum += number * (ord(first_letter) - 96)
    if last_letter.isupper():
        total_sum -= (ord(last_letter) - 64)
    elif last_letter.islower():
        total_sum += (ord(last_letter) - 96)
print(f"{total_sum:.2f}")