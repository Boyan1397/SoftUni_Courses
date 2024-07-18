def draw_cards(*args, **kwargs):
    cards_dict = {"monster": [], "spell": []}

    for name, c_type in args:
        if name not in cards_dict[c_type]:
            cards_dict[c_type].append(name)

    for name, c_type in kwargs.items():
        if name not in cards_dict[c_type]:
            cards_dict[c_type].append(name)

    cards_dict["monster"] = sorted(cards_dict["monster"], reverse= True)
    cards_dict["spell"] = sorted(cards_dict["spell"])

    output = ""
    if cards_dict["monster"]:
        output += "Monster cards:\n"
        for card in cards_dict["monster"]:
            output += f"  ***{card}\n"

    if cards_dict["spell"]:
        output += "Spell cards:\n"
        for card in cards_dict["spell"]:
            output += f"  $$${card}\n"

    return output.strip()


print(draw_cards(("celtic guardian", "monster"),

("earthquake", "spell"),

("fireball", "spell"),

raigeki="spell", destroy="spell",))


# Monster cards:
#   ***celtic guardian
# Spell cards:
#   $$$destroy
#   $$$earthquake
#   $$$fireball
#   $$$raigeki