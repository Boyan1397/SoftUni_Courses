activation_key_input = input()

command = input()
while "Generate" not in command:
    if "Contains" in command:
        substring = command.split(">>>")[1]
        if substring in activation_key_input:
            print(f"{activation_key_input} contains {substring}")
        else:
            print("Substring not found!")
    elif "Flip" in command:
        upper_or_lower = command.split(">>>")[1]
        start_index = int(command.split(">>>")[2])
        end_index = int(command.split(">>>")[3])
        between_indexes = (activation_key_input[start_index:end_index])
        if upper_or_lower == "Upper":
            activation_key_input = activation_key_input[:start_index] + between_indexes.upper() + activation_key_input[end_index:]
            print(activation_key_input)
        elif upper_or_lower == "Lower":
            activation_key_input = activation_key_input[:start_index] + between_indexes.lower() + activation_key_input[end_index:]
            print(activation_key_input)
    elif "Slice" in command:
        start_index = int(command.split(">>>")[1])
        end_index = int(command.split(">>>")[2])
        activation_key_input = activation_key_input[:start_index] + activation_key_input[end_index:]
        print(activation_key_input)
    command = input()

print(f"Your activation key is: {activation_key_input}")


