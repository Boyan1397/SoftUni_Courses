all_friends = input().split(", ")
command = input()
blacklisted_names = 0
lost_names = 0
while command != "Report":
    list_of_actions = command.split(" ")
    action = list_of_actions[0]
    name = list_of_actions[1]
    if action == "Blacklist":
        if name in all_friends:
            print(f"{name} was blacklisted.")
            all_friends[all_friends.index(name)] = "Blacklisted"
            blacklisted_names += 1
            break
        else:
            print(f"{name} was not found")
    elif action == "Error":
        index = int(command[1])
        if name != "Blacklisted" and name != "Lost":
            if len(all_friends) > index >= 0:
                name = all_friends[index]
                all_friends[index] = "Lost"
                lost_names += 1
                print(f"{name} was lost due to error.")
    elif action == "Change":
        last_name = (command[2])
        index = int(command[1])
        if len(all_friends) > index >= 0:
            actual_name = all_friends[index]
            all_friends[index] = last_name
            print(f"{actual_name} changed his username to {last_name}")

print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(" ".join(all_friends))




