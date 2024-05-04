my_string = input()
last_letter = ''
final_string = ''
#aaaaabbbbbcdddeeeedssaa
for current_letter in my_string:
    if last_letter != current_letter:
        final_string += current_letter
        last_letter = current_letter
print(final_string)