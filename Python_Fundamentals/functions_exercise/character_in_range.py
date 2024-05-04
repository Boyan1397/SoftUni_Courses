def all_characters(first,second):
    characters = []
    for current_characters_as_digits in range(ord(first)+1,ord(second)):
        characters.append(chr(current_characters_as_digits))
    return characters





first_input = input()
second_input = input()
print(" ".join(all_characters(first_input, second_input)))