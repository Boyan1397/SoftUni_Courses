my_string = input()
final_string = ""
strength = 0
#abv>1>1>2>2asdasd
for index in range(len(my_string)):
    if my_string[index] == ">":
        final_string += my_string[index]
        strength += int(my_string[index+1])
    elif my_string[index] != ">" and strength > 0:
        strength -= 1
    elif my_string[index] != ">" and strength == 0:
        final_string += my_string[index]
print(final_string)