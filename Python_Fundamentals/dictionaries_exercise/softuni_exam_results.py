results_dict = {}
submissions_dict = {}
command = input().split("-")
while len(command) != 1:

    if len(command) == 3:
        count = 0
        username, language, points = command[0], command[1], int(command[2])
        if username not in results_dict.keys():
            results_dict[username] = 0
        if points > results_dict[username]:
            results_dict[username] = points
        if language not in submissions_dict.keys():
            submissions_dict[language] = 0
        submissions_dict[language] += 1

    elif len(command) == 2:
        username = command[0]
        if username in results_dict.keys():
            del results_dict[username]

    command = input().split("-")

print("Results:")
for key, value in results_dict.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in submissions_dict.items():
    print(f"{key} - {value}")