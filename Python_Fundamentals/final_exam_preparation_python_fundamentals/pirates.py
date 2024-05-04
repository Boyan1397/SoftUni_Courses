towns_info = {}

command = input()
while command != "Sail":
    town, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)
    if town not in towns_info:
        towns_info[town] = {"population": population, "gold": gold}
    elif town in towns_info:
        towns_info[town]["population"] += population
        towns_info[town]["gold"] += gold
    command = input()

command = input()
while command != "End":
    if "Plunder" in command:
        town = command.split("=>")[1]
        population = int(command.split("=>")[2])
        gold = int(command.split("=>")[3])
        towns_info[town]["population"] -= population
        towns_info[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {population} citizens killed.")
        if towns_info[town]["population"] <= 0 or towns_info[town]["gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            del towns_info[town]

    elif "Prosper" in command:
        town = command.split("=>")[1]
        gold = int(command.split("=>")[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            towns_info[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns_info[town]['gold']} gold.")

    command = input()
if not towns_info:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(towns_info.keys())} wealthy settlements to go to:")
for town_name, values in towns_info.items():
    print(f"{town_name} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")