material_dict = {"shards": 0, "fragments": 0, "motes": 0}
is_obtained = False
entry = input().split()
while not is_obtained:
    for index in range(0, len(entry), 2):
        quantity = int(entry[index])
        material = entry[index+1].lower()
        if material not in material_dict.keys():
            material_dict[material] = 0
        material_dict[material] += quantity

        if material_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            material_dict["shards"] -= 250
            is_obtained = True

        elif material_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            material_dict["fragments"] -= 250
            is_obtained = True

        elif material_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            material_dict["motes"] -= 250
            is_obtained = True

        if is_obtained:
            break
    if is_obtained:
        break

    entry = input().split()
for key, value in material_dict.items():
    print(f"{key}: {value}")



