my_string = input().upper()
final_string = ""
current_string= ""
repetitions = ""

for index in range(len(my_string)):
    if not my_string[index].isdigit():
        current_string += my_string[index]
    elif my_string[index].isdigit():
        for number_index in range(index, len(my_string)):
            if my_string[number_index].isdigit():
                repetitions += str(my_string[number_index])
            else:
                break
        final_string += current_string * int(repetitions)
        current_string = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)