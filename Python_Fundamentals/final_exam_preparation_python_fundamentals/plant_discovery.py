my_dict = {}
n_lines = int(input())
for _ in range(n_lines):
    data_info = input()
    plant = data_info.split("<->")[0]
    rarity = data_info.split("<->")[1]
    if plant not in my_dict:
        my_dict[plant] = {"rarity": [], "rating": []}
        my_dict[plant]["rarity"].append(rarity)
    elif plant in my_dict:
        my_dict[plant]["rarity"] = [rarity]

command = input()
while command != "Exhibition":
    if "Rate" in command:
        plant_and_rating = command.split(": ")[1]
        plant = plant_and_rating.split(" - ")[0]
        rating = plant_and_rating.split(" - ")[1]
        if plant in my_dict:
            my_dict[plant]["rating"].append(int(rating))
        else:
            print("error")
    elif "Update" in command:
        plant_and_rating = command.split(": ")[1]
        plant = plant_and_rating.split(" - ")[0]
        new_rarity = plant_and_rating.split(" - ")[1]
        if plant in my_dict:
            my_dict[plant]["rarity"] = [new_rarity]
        else:
            print("error")
    elif "Reset" in command:
        plant_and_rating = command.split(": ")[1]
        plant = plant_and_rating.split(" - ")[0]
        if plant in my_dict.keys():
            my_dict[plant]["rating"].clear()
        else:
            print("error")

    command = input()


print("Plants for the exhibition:")
for plant, values in my_dict.items():
    if not my_dict[plant]["rating"]:
        my_dict[plant]["rating"] = [0]
    average_rating = sum(values['rating']) / len(values['rating'])
    print(f"- {plant}; Rarity: {', '.join((values['rarity']))}; Rating: {average_rating:.2f}")