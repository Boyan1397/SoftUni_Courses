n_lines = int(input())
my_dict = {}
for _ in range(n_lines):
    command = input().split()
    if "register" == command[0]:
        username, number = command[1], command[2]
        if username not in my_dict.keys():
            my_dict[username] = number
            print(f"{username} registered {my_dict[username]} successfully")
        elif username in my_dict.keys():
            print(f"ERROR: already registered with plate number {my_dict[username]}")

    elif "unregister" == command[0]:
        username = command[1]
        if username not in my_dict.keys():
            print(f"ERROR: user {username} not found")
        elif username in my_dict.keys():
            del my_dict[username]
            print(f"{username} unregistered successfully")

for name, plate in my_dict.items():
    print(f"{name} => {plate}")

