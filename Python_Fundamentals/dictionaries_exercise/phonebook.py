my_dict = {}
while True:
    entry = input()
    if entry.isdigit():
        break
    name, number = entry.split("-")
    if name not in my_dict.keys():
        my_dict[name] = number
    else:
        my_dict[name] = number

n_lines = int(entry)
for _ in range(n_lines):
    searched_name = input()
    if searched_name in my_dict.keys():
        print(f"{searched_name} -> {my_dict[searched_name]}")

    elif searched_name not in my_dict:
        print(f"Contact {searched_name} does not exist.")
