my_message = input()

command = input()
while command != "Reveal":
    if "InsertSpace" in command:
        index = int(command.split(":|:")[1])
        my_message = my_message[:index] + " " + my_message[index:]
        print(my_message)
    elif "Reverse" in command:
        substring = command.split(":|:")[1]
        if substring not in my_message:
            print("error")
        elif substring in my_message:
            my_message = my_message.replace(substring, "",1)
            my_message = my_message + substring[::-1]
            print(my_message)
    elif "ChangeAll" in command:
        substring = command.split(":|:")[1]
        replacement = command.split(":|:")[2]
        my_message = my_message.replace(substring, replacement)
        print(my_message)

    command = input()
print(f"You have a new text message: {my_message}")
