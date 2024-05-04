text = ""

command = input()
while command != "End":
    if "Add" in command:
        substring = command.split()[1]
        text += substring
    elif "Upgrade" in command:
        char = command.split()[1]
        ascii_char = ord(char) + 1
        final_char = chr(ascii_char)
        text = text.replace(char, final_char)
    elif "Print" in command:
        print(text)
    elif "Index" in command:
        char_index = command.split()[1]
        indexes = [index for index in range(len(text)) if text[index] == char_index]
        if indexes:
            print(*indexes)
        else:
            print("None")
    elif "Remove" in command:
        substring = command.split()[1]
        text = text.replace(substring, "")
    command = input()
