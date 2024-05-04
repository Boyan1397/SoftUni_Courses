def chars_in_range(first, second):
    list_ords = []
    list_chars = []
    for elements in range(ord(first) + 1, ord(second)):
        list_ords.append(elements)
    for ords in list_ords:
        list_chars.append(chr(ords))
    return list_chars



first_character = input()
second_character = input()
result = (" ".join(chars_in_range(first_character, second_character)))
print(result)