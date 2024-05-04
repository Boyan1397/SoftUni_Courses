from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars_queue = deque()
count = 0

command = input()
while command != "END":
    if command != "green":
        cars_queue.append(command)
    elif command == "green":
        current_green_light = green_light_duration

        while current_green_light > 0 and cars_queue:
            car = cars_queue.popleft()
            time_to_pass = current_green_light + free_window_duration
            if time_to_pass < len(car):
                print("A crash happened!")
                print(f"{car} was hit at {car[time_to_pass]}.")
                exit()
            else:
                current_green_light -= len(car)
                count += 1
    command = input()

print("Everyone is safe.")
print(f"{count} total cars passed the crossroads.")