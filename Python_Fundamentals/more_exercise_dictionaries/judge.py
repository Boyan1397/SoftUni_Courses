contest_dict = {}
command = input()
individual_standings = {}
while command != "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)
    if contest not in contest_dict:
        contest_dict[contest] = {}
    if username not in contest_dict[contest]:
        contest_dict[contest][username] = points
    else:
        if contest_dict[contest][username] < points:
            contest_dict[contest][username] = points
    command = input()


for name in contest_dict.keys():
    second_dict_values = contest_dict[name]
    print(f"{name}: {len(second_dict_values)} participants")
    for pos, (key, value) in enumerate(sorted(second_dict_values.items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{pos}. {key} <::> {value}")

new_dictionary = {}

for individual_name in individual_standings.keys():
    second_dict = individual_standings[individual_name]
    sum_points = sum(second_dict.values())
    new_dictionary[individual_name] = sum_points

print(f"Individual standings:")
el1 = 1
for position, (key, value) in enumerate(sorted(new_dictionary.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{position}. {key} -> {value}")