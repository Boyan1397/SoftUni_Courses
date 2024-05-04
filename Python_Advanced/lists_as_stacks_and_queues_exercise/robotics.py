from collections import deque
from datetime import datetime, timedelta

robots_data = input().split(";")
starting_time = datetime.strptime(input(), "%H:%M:%S")
robots_dict = {}

for r in robots_data:
    name, seconds_to_do = r.split("-")
    robots_dict[name] = [int(seconds_to_do), 0]

products = deque()
command = input()
while command != "End":
    products.append(command)
    command = input()

while products:
    product = products.popleft()
    starting_time += timedelta(seconds=1)

    free_robots = deque()
    for name, values in robots_dict.items():
        if robots_dict[name][1] > 0:
            robots_dict[name][1] -= 1

        if robots_dict[name][1] == 0:
            free_robots.append(name)

    if not free_robots:
        products.append(product)
        continue
    if free_robots:
        free_robot = free_robots.popleft()
        robots_dict[free_robot][1] = robots_dict[free_robot][0]
        print(f"{free_robot} - {product} [{starting_time.strftime('%H:%M:%S')}]")