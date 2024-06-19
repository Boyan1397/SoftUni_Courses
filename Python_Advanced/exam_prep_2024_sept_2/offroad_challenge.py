from collections import deque

initial_fuel = [int(el) for el in input().split()] #last
add_consumption_index = deque(int(el) for el in input().split()) #first
fuel_needed = deque(int(el) for el in input().split()) #first

max_len = len(fuel_needed)

altitude_counter = 0
str_alt_counter = []
reached_the_top = False

while initial_fuel and add_consumption_index and fuel_needed:
    init_fuel = initial_fuel[-1]
    cons_index = add_consumption_index[0]
    needed = fuel_needed[0]
    if (init_fuel - cons_index) >= needed:
        initial_fuel.pop()
        add_consumption_index.popleft()
        fuel_needed.popleft()
        altitude_counter += 1
        print(f"John has reached: Altitude {altitude_counter}")
        if max_len == altitude_counter:
            reached_the_top = True
            break
    else:
        print(f"John did not reach: Altitude {altitude_counter + 1}")
        break

if not reached_the_top and altitude_counter >= 1:
    print("John failed to reach the top.\n"
          f"Reached altitudes: {', '.join([f'Altitude {el}' for el in range(1, altitude_counter + 1)])}")

elif not reached_the_top and altitude_counter == 0:
    print("John failed to reach the top.\n"
          "John didn't reach any altitude.")
if reached_the_top:
    print("John has reached all the altitudes and managed to reach the top!")