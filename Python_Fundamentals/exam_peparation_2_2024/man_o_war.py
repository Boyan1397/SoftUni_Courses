def is_index_valid(ship_status, given_index):
    if given_index in range(len(ship_status)):
        return True
    return False


def after_fire(warship_status_list, some_index, damage_number):
    if is_index_valid(warship_status_list, some_index):
        warship_status_list[some_index] -= damage_number
        if warship_status_list[some_index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit(0)
    return warship_status_list


def after_defending(pirate_ship_list, start_index, end_index, damage_number):
    if is_index_valid(pirate_ship_list, start_index):
        if is_index_valid(pirate_ship_list, end_index):
            for idx in range(start_index, end_index +1):
                pirate_ship_list[idx] -= damage_number
                if pirate_ship_list[idx] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)
    return pirate_ship_list


def after_repairing(pirate_ship_list, some_index, some_health, max_health):
    if is_index_valid(pirate_ship_list, some_index):
        pirate_ship_list[some_index] += some_health
        if pirate_ship_list[some_index] >= max_health:
            pirate_ship_list[some_index] = max_health
    return pirate_ship_list


pirate_ship_status = [int(el) for el in input().split(">")]
warship_status = [int(el) for el in input().split(">")]
maximum_health = int(input())

command = input()
while command != "Retire":
    current_command = command.split()[0]
    if current_command == "Fire":
        index, damage = int(command.split()[1]), int(command.split()[2])
        fire_list = after_fire(warship_status, index, damage)
        warship_status = fire_list

    elif current_command == "Defend":
        index_first, index_second, defense_damage = int(command.split()[1]), int(command.split()[2]), int(command.split()[3])
        defence_list = after_defending(pirate_ship_status, index_first, index_second, defense_damage)
        pirate_ship_status = defence_list

    elif current_command == "Repair":
        index, healing = int(command.split()[1]), int(command.split()[2])
        heal_list = after_repairing(pirate_ship_status, index, healing, maximum_health)
        pirate_ship_status = heal_list

    elif current_command == "Status":
        percentage = 0.20 * maximum_health
        needed_repair = [section for section in pirate_ship_status if section < percentage]
        print(f"{len(needed_repair)} sections need repair.")
    command = input()

print(f"Pirate ship status: {sum(pirate_ship_status)}")
print(f"Warship status: {sum(warship_status)}")
