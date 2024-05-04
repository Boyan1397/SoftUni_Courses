total_energy = 100
total_coins = 100
events = input().split('|')
is_working = True
for event in events:
    big_event = event.split("-")
    ingredient = big_event[0]
    event_number = big_event[1]

    if ingredient == "rest":
        current_energy = total_energy
        total_energy += int(event_number)
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif ingredient == "order":
        if total_energy >= 30:
            total_coins += int(event_number)
            total_energy -= 30
            print(f"You earned {int(event_number)} coins.")
        else:
            print("You had to rest!")
            total_energy += 50
    else:
        if total_coins >= int(event_number):
            print(f"You bought {ingredient}.")
            total_coins -= int(event_number)
        else:
            is_working = False
            break

if is_working:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {ingredient}.")
