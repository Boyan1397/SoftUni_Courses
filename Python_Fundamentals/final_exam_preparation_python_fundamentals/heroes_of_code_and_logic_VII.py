my_dict = {}
n_lines = int(input())
for _ in range(n_lines):
    data_info = input()
    name = data_info.split()[0]
    hp = int(data_info.split()[1])
    mana = int(data_info.split()[2])
    if name not in my_dict:
        my_dict[name] = {"hp": hp, "mana": mana}

command = input()
while command != "End":
    if "CastSpell" in command:
        hero_name = command.split(" - ")[1]
        mana_needed = int(command.split(" - ")[2])
        spell = command.split(" - ")[3]
        if my_dict[hero_name]["mana"] < mana_needed:
            print(f"{hero_name} does not have enough MP to cast {spell}!")
        elif my_dict[hero_name]["mana"] >= mana_needed:
            print(f"{hero_name} has successfully cast {spell} and now has {my_dict[hero_name]['mana'] - mana_needed} MP!")
            my_dict[hero_name]['mana'] -= mana_needed
    elif "TakeDamage" in command:
        hero_name = command.split(" - ")[1]
        damage = int(command.split(" - ")[2])
        attacker = command.split(" - ")[3]
        if my_dict[hero_name]["hp"] - damage <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
            del my_dict[hero_name]
        elif my_dict[hero_name]["hp"] - damage > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {my_dict[hero_name]['hp'] - damage} HP left!")
            my_dict[hero_name]['hp'] -= damage
    elif "Recharge" in command:
        hero_name = command.split(" - ")[1]
        amount_mana = int(command.split(" - ")[2])
        if my_dict[hero_name]["mana"] + amount_mana >= 200:
            print(f"{hero_name} recharged for {200 - my_dict[hero_name]['mana']} MP!")
            my_dict[hero_name]['mana'] = 200
        elif my_dict[hero_name]["mana"] + amount_mana < 200:
            print(f"{hero_name} recharged for {amount_mana} MP!")
            my_dict[hero_name]["mana"] += amount_mana
    elif "Heal" in command:
        hero_name = command.split(" - ")[1]
        amount_hp = int(command.split(" - ")[2])
        if my_dict[hero_name]["hp"] + amount_hp >= 100:
            print(f"{hero_name} healed for {100 - my_dict[hero_name]['hp']} HP!")
            my_dict[hero_name]['hp'] = 100
        elif my_dict[hero_name]["hp"] + amount_hp < 100:
            print(f"{hero_name} healed for {amount_hp} HP!")
            my_dict[hero_name]["hp"] += amount_hp
    command = input()

for name, values in my_dict.items():
    print(f"{name}")
    print(f"  HP: {my_dict[name]['hp']}")
    print(f"  MP: {my_dict[name]['mana']}")