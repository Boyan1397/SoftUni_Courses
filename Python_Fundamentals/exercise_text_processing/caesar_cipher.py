words = input()
final_string = ""
for word in words:
    numbers = ord(word) + 3
    final_string += chr(numbers)
print(final_string)