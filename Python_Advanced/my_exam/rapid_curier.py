from collections import deque

my_packages = [int(el) for el in input().split()]
my_couriers = deque([int(el) for el in input().split()])
all_weight = 0

while my_packages and my_couriers:
    my_capacity = my_couriers[0]
    weight = my_packages[-1]
    if my_capacity >= weight:

        my_capacity -= (weight * 2)
        all_weight += weight

        if my_capacity > 0:
            my_couriers.popleft()
            my_couriers.append(my_capacity)
        else:
            my_couriers.popleft()
        my_packages.pop()

    else:
        weight -= my_capacity
        my_couriers.popleft()
        my_packages.pop()
        my_packages.append(weight)
        all_weight += my_capacity

print(f"Total weight: {all_weight} kg")

if not my_packages and not my_couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today." )

if my_couriers and not my_packages:
    print(f"Couriers are still on duty: {', '.join(str(el) for el in my_couriers)} but there are no more packages to deliver.")

if my_packages and not my_couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(el) for el in my_packages)}")



# 13 11 7
# 5 11