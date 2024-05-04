race_inputs = [int(num) for num in input().split()]

middle = len(race_inputs) // 2
first_part = race_inputs[:middle]
second_part = race_inputs[middle:]
left_car = 0
right_car = 0
for i in first_part:
    left_car += i
    if i == 0:
        left_car *= 0.80
for n in second_part:
    right_car += n
    if n == 0:
        right_car *= 0.8
if left_car < right_car:
    print(f"The winner is left with total time: {left_car:.1f}")
else:
    print(f"The winner is right with total time: {right_car:.1f}")



