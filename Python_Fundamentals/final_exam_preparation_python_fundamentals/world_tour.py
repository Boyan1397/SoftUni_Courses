my_stops = input()

command = input()
while command != "Travel":
    if "Add Stop" in command:
        index = int(command.split(":")[1])
        some_string = command.split(":")[2]
        if index in range(len(my_stops)):
            my_stops = my_stops[:index] + some_string + my_stops[index:]
        print(my_stops)
    elif "Remove Stop" in command:
        start_index = int(command.split(":")[1])
        end_index = int(command.split(":")[2])
        if start_index in range(len(my_stops)) and end_index in range(len(my_stops)):
            my_stops = my_stops[:start_index] + my_stops[end_index+1:]
        print(my_stops)
    elif "Switch" in command:
        old_string = command.split(":")[1]
        new_string = command.split(":")[2]
        if old_string in my_stops:
            my_stops = my_stops.replace(old_string, new_string)
        print(my_stops)

    command = input()
print(f"Ready for world tour! Planned stops: {my_stops}")