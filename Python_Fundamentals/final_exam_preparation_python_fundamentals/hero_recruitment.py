my_dict = {}

command = input()
while command != "End":
    if "Enroll" in command:
        name = command.split()[1]
        if name not in my_dict:
            my_dict[name] = []
        else:
            print(f"{name} is already enrolled.")
    elif "Learn" in command:
        name = command.split()[1]
        spell = command.split()[2]
        if name not in my_dict:
            print(f"{name} doesn't exist.")
        elif spell not in my_dict[name]:
            my_dict[name].append(spell)
        else:
            print(f"{name} has already learnt {spell}.")
    elif "Unlearn" in command:
        name = command.split()[1]
        spell = command.split()[2]
        if name not in my_dict:
            print(f"{name} doesn't exist.")
        elif spell not in my_dict[name]:
            print(f"{name} doesn't know {spell}.")
        else:
            my_dict[name].remove(spell)

    command = input()
print("Heroes:")
for names, values in my_dict.items():
    print(f"== {names}: {' '.join(values)}")

