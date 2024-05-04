my_dict = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        force_side, username = command.split(" | ")
        is_found = False
        for value in my_dict.values():
            if username in value:
                is_found = True
                break
        if not is_found:
            if force_side not in my_dict.keys():
                my_dict[force_side] = []
            my_dict[force_side].append(username)

    elif "->" in command:
        username, force_side = command.split(" -> ")
        if force_side not in my_dict.keys():
            my_dict[force_side] = []
        for value in my_dict.values():
            if username in value:
                value.remove(username)
        if username not in my_dict.values():
            my_dict[force_side].append(username)

        print(f"{username} joins the {force_side} side!")
    command = input()

for key, values in my_dict.items():
    if len(my_dict[key]) != 0:
        print(f"Side: {key}, Members: {len(my_dict[key])}")
    for value in values:
        print(f"! {value}")