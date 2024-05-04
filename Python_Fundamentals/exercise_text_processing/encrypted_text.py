text = input()
final_string = ""
for character in text:
    final_character = chr(ord(character) + 3)
    final_string += final_character
print(*final_string,sep= "")