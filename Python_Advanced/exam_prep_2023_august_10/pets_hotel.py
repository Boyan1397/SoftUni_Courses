def accommodate_new_pets(capacity, max_weight, *args):
    my_pets = {}
    are_accommodated = True
    for p_type, weight in args:
        if capacity > 0:
            if weight > max_weight:
                continue
            if p_type not in my_pets.keys():

                my_pets[p_type] = []
            capacity -= 1
            my_pets[p_type].append(weight)
        else:
            are_accommodated = False
            break

    output = ""
    sorted_pets = dict(sorted(my_pets.items(), key= lambda x: x[0]))
    if are_accommodated:
        output += f"All pets are accommodated! Available capacity: {capacity}.\n"
        output += "Accommodated pets:\n"
        for p_type, value in sorted_pets.items():
            output += f"{p_type}: {len(value)}\n"
    else:
        output += "You did not manage to accommodate all pets!\n"
        output += "Accommodated pets:\n"
        for p_type, value in sorted_pets.items():
            output += f"{p_type}: {len(value)}\n"



    return output.strip()











print(accommodate_new_pets(
10,
15.0,
("cat", 5.8),
("dog", 10.0),
))


# print(accommodate_new_pets( 10, 10.0, ("cat", 5.8), ("dog", 10.5), ("parrot", 0.8), ("cat", 3.1), ))


# print(accommodate_new_pets(
#
# 2,
#
# 15.0,
#
# ("dog", 10.0),
#
# ("cat", 5.8),
#
# ("cat", 2.7),
#
# ))