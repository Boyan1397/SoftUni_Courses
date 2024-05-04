number_of_balls = int(input())
weight_of_balls = 0
time_of_balls = 0
quality_of_balls = 0
value_of_balls = 0
for ball in range(number_of_balls):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > value_of_balls:
        value_of_balls = value
        weight_of_balls = weight
        time_of_balls = time
        quality_of_balls = quality
print(f"{weight_of_balls} : {time_of_balls} = {(value_of_balls)} ({quality_of_balls})")
