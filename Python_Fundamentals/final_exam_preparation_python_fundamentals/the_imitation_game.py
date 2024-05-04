encrypted_message = input()

command = input()
while command != "Decode":
    if "Move" in command:
        n_letters = int(command.split("|")[1])
        encrypted_message = encrypted_message[n_letters:] + encrypted_message[:n_letters]
    elif "Insert" in command:
        index = int(command.split("|")[1])
        value = command.split("|")[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif "ChangeAll" in command:
        substring = command.split("|")[1]
        replacement = command.split("|")[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()
print(f"The decrypted message is: {encrypted_message}")