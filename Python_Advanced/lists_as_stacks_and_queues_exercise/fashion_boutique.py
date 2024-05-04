box_with_clothes = [int(el) for el in input().split()]
capacity_of_rack = int(input())


rack = 1
sum_of_clothes = 0
current_capacity = capacity_of_rack
while box_with_clothes:
    cloth = box_with_clothes.pop()
    if current_capacity >= cloth:
        current_capacity -= cloth
        sum_of_clothes += cloth
    elif current_capacity < cloth:
        rack += 1
        current_capacity = capacity_of_rack - cloth
print(rack)