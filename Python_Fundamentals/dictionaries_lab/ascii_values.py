list_of_characters = input().split(", ")
char_dict = {element: ord(element) for element in list_of_characters}
print(char_dict)
