def naughty_or_nice_list(santa_list, *args, **kwargs):
    kids_dict = {"Nice": [], "Naughty": [],"Not found": []}
    for arg in args:
        number, k_type = arg.split("-")
        count_numbers = [tuple_data for tuple_data in santa_list if tuple_data[0] == int(number)]
        if len(count_numbers) == 1:
            kids_dict[k_type].append(count_numbers[0][1])
            santa_list.remove(*count_numbers)

    for name, kd_type in kwargs.items():
        count_names = [tuple_data for tuple_data in santa_list if name == tuple_data[1]]
        if len(count_names) == 1:
            kids_dict[kd_type].append(count_names[0][1])
            santa_list.remove(*count_names)

    if santa_list:
        for tup in santa_list:
            kids_dict["Not found"].append(tup[1])
    output = ""
    for key, values in kids_dict.items():
        if values:
            output += f"{key}: {', '.join(kids_dict[key])}\n"
    return output

# [(3, 'Amy'), (7, 'George'), (3, 'Katy')] list
# ('3-Nice', '1-Naughty') args
# {'Amy': 'Nice', 'Katy': 'Naughty'} kwargs


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
 [
 (7, "Peter"),
 (1, "Lilly"),
 (2, "Peter"),
 (12, "Peter"),
 (3, "Simon"),
 ],
 "3-Nice",
 "5-Naughty",
 "2-Nice",
 "1-Nice",
 ))