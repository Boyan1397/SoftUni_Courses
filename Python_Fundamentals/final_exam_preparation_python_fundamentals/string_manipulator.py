text = input()

command = input()
while command != "End":
    if "Translate" in command:
        char = command.split()[1]
        replacement = command.split()[2]
        text = text.replace(char, replacement)
        print(text)
    elif "Includes" in command:
        substring = command.split()[1]
        if substring in text:
            print("True")
        else:
            print("False")
    elif "Start" in command:
        substring = command.split()[1]
        if text.startswith(substring):
            print("True")
        else:
            print("False")
    elif "Lowercase" in command:
        text = text.lower()
        print(text)
    elif "FindIndex" in command:
        char = command.split()[1]
        print(text.rfind(char))
    elif "Remove" in command:
        start_index = int(command.split()[1])
        count = int(command.split()[2])
        text = text[:start_index] + text[start_index+ count:]
        print(text)

    command = input()