import math

number_of_students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_list = []
attendances_list = []
for students in range(1, number_of_students +1):
    attendance_for_each = int(input())
    total_bonus = attendance_for_each / lectures * (5 + additional_bonus)
    max_list.append(total_bonus)
    max_bonus = max(max_list)
    attendances_list.append(attendance_for_each)
    max_attendances = max(attendances_list)
print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")