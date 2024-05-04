n_lines = int(input())
my_cars_dict = {}
for _ in range(n_lines):
    first_command = input()
    brand = first_command.split("|")[0]
    mileages = int(first_command.split("|")[1])
    range_fuel = int(first_command.split("|")[2])
    if brand not in my_cars_dict:
        my_cars_dict[brand] = {"mileages": mileages, "fuel_range": range_fuel}

command = input()
while command != "Stop":
    if "Drive" in command:
        brand = command.split(" : ")[1]
        distance = int(command.split(" : ")[2])
        fuel = int(command.split(" : ")[3])

        if my_cars_dict[brand]["fuel_range"] - fuel <= 0:
            print("Not enough fuel to make that ride")
        elif my_cars_dict[brand]["fuel_range"] - fuel > 0:
            my_cars_dict[brand]["mileages"] += distance
            my_cars_dict[brand]["fuel_range"] -= fuel
            print(f"{brand} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if my_cars_dict[brand]["mileages"] >= 100000:
            del my_cars_dict[brand]
            print(f"Time to sell the {brand}!")

    elif "Refuel" in command:
        brand = command.split(" : ")[1]
        refill_fuel = int(command.split(" : ")[2])
        if my_cars_dict[brand]["fuel_range"] + refill_fuel >= 75:
            print(f"{brand} refueled with {75 - my_cars_dict[brand]['fuel_range']} liters")
            my_cars_dict[brand]["fuel_range"] = 75
        elif my_cars_dict[brand]["fuel_range"] + refill_fuel < 75:
            my_cars_dict[brand]["fuel_range"] += refill_fuel
            print(f"{brand} refueled with {refill_fuel} liters")
    elif "Revert" in command:
        brand = command.split(" : ")[1]
        kilometers = int(command.split(" : ")[2])
        if my_cars_dict[brand]["mileages"] - kilometers <= 10000:
            my_cars_dict[brand]["mileages"] = 10000
        elif my_cars_dict[brand]["mileages"] - kilometers > 10000:
            my_cars_dict[brand]["mileages"] -= kilometers
            print(f"{brand} mileage decreased by {kilometers} kilometers")

    command = input()

for brand, values in my_cars_dict.items():
    print(f"{brand} -> Mileage: {my_cars_dict[brand]['mileages']} kms, Fuel in the tank: {my_cars_dict[brand]['fuel_range']} lt.")
