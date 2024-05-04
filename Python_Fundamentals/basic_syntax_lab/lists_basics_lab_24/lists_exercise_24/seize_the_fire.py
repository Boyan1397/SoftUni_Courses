list_of_fire = input().split("#")
water = int(input())
effort = 0
final_fire = 0

print("Cells:")
for fire in list_of_fire:
    total_fire = fire.split(" = ")
    level_fire = total_fire[0]
    amount_fire = int(total_fire[1])
    condition = False
    if level_fire == "High":
        if 81 <= amount_fire <= 125:
            condition = True

    elif level_fire == "Medium":
        if 51 <= amount_fire <= 80:
            condition = True

    elif level_fire == "Low":
        if 1 <= amount_fire <= 50:
            condition = True

    if condition:
        if water >= amount_fire:
            water -= amount_fire
            final_fire += amount_fire
            effort += amount_fire * 0.25
            print(f" - {amount_fire}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {final_fire}")
