command = input()
importance_list = [0] * 10
while command != "End":
    command_info = command.split("-")
    importance = int(command_info[0])
    index = importance - 1
    action = command_info[1]
    importance_list[index] = action
    final_list = [el for el in importance_list if el != 0]
    command = input()
print(final_list)
