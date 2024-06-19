from collections import deque

initial_fuel = input().split() #last
add_consumption_index = deque(input().split()) #first
fuel_needed = deque(input().split()) #first
fuel_needed_len = len(fuel_needed)

altitude_counter = 0
str_alt_counter = []
reached_the_top = False

while initial_fuel:
    init_fuel = int(initial_fuel.pop())
    consumption_idx = int(add_consumption_index.popleft())
    needed_fuel = int(fuel_needed.popleft())

    if (init_fuel - consumption_idx) >= needed_fuel:
        altitude_counter += 1
        str_alt_counter.append(f"Altitude {altitude_counter}")
        print(f"John has reached: Altitude {altitude_counter}")
        if fuel_needed_len == altitude_counter:
            reached_the_top = True
            break
    elif (init_fuel - consumption_idx) < needed_fuel:
        print(f"John did not reach: Altitude {altitude_counter + 1}")
        if altitude_counter > 0:
            print(f"John failed to reach the top.\n"
                  f"Reached altitudes: {', '.join(str_alt_counter)}")
            break
        else:
            print("John failed to reach the top.\n"
                  "John didn't reach any altitude.")
            break

if reached_the_top:
    print("John has reached all the altitudes and managed to reach the top!")