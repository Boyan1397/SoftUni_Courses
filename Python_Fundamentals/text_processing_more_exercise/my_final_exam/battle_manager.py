my_dict = {}
battle = ""
command = input()
while command != "Results":
    if "Add" in command:
        name = command.split(":")[1]
        health = int(command.split(":")[2])
        energy = int(command.split(":")[3])
        if name not in my_dict:
            my_dict[name] = {"health": health, "energy": energy}
        elif name in my_dict:
            my_dict[name]["health"] += health
    elif "Attack" in command:
        attacker_name = command.split(":")[1]
        defender_name = command.split(":")[2]
        damage = int(command.split(":")[3])
        if attacker_name in my_dict and defender_name in my_dict:
            my_dict[defender_name]["health"] -= damage
            my_dict[attacker_name]["energy"] -= 1
            if my_dict[defender_name]["health"] <= 0:
                print(f"{defender_name} was disqualified!")
                del my_dict[defender_name]
            if my_dict[attacker_name]["energy"] <= 0:
                print(f"{attacker_name} was disqualified!")
                del my_dict[attacker_name]
    elif "Delete" in command:
        username = command.split(":")[1]
        if username == "All":
            my_dict.clear()
        elif username in command:
            del my_dict[username]

    command = input()
print(f"People count: {len(my_dict.keys())}")
for names, values in my_dict.items():
    print(f"{names} - {my_dict[names]['health']} - {my_dict[names]['energy']}")





# Add:Mark:1000: 5
# Add:Clark:1000: 2
# Attack:Clark:Mark: 500
# Attack:Clark:Mark: 800
# Add:Charlie:4000: 10
# Results
# Add:Bonnie:3000:5
# Add:Kent:10000:10
# Add:Johny:4000:10
# Attack:Johny:Bonnie:400
# Add:Johny:3000:5
# Add:Peter:7000:1
# Delete:Kent
# Results

