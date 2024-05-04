health = 100
bitcoins = 0
MAX_HEALTH = 100
dungeon_rooms = input().split("|")
room_counter = 0
is_alive = True
for room in dungeon_rooms:
    room_counter += 1
    command_input = room.split()
    action, number = command_input[0], int(command_input[1])
    if action == "potion":
        if health + number > MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health = MAX_HEALTH
        else:
            print(f"You healed for {number} hp.")
            health += number
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {room_counter}")
            is_alive = False
            break
if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
