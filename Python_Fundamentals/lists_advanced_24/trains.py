train = [0] * int(input())

command = input()
while command != "End":
    command_info = command.split(" ")
    action = command_info[0]
    if action == "add":
        people = int(command_info[1])
        train[-1] += people
    elif action == "insert":
        index = int(command_info[1])
        n_people = int(command_info[2])
        train[index] += n_people
    elif action == "leave":
        index = int(command_info[1])
        n_people = int(command_info[2])
        train[index] -= n_people

    command = input()
print(train)