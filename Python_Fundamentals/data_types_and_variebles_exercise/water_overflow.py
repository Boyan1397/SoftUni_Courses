tank_capacity = 255
number_of_lines = int(input())
water_counter = 0
for num in range(number_of_lines):
    current_water = int(input())
    if (tank_capacity - current_water) >= 0:
        tank_capacity -= current_water
        water_counter += current_water
    else:
        print("Insufficient capacity!")
print(water_counter)