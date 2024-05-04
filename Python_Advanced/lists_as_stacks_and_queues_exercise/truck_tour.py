from collections import deque

n_pumps = int(input())
pumps_queue = deque()
index = 0
my_petrol = 0

for _ in range(n_pumps):
    pump_data = [int(s) for s in input().split()]
    pumps_queue.append(pump_data)

pumps_queue_copy = pumps_queue.copy()
while pumps_queue_copy:
    current_pump = pumps_queue_copy.popleft()
    amount_petrol = current_pump[0]
    distance = current_pump[1]
    my_petrol += amount_petrol
    if my_petrol >= distance:
        my_petrol -= distance
    elif my_petrol < distance:
        pumps_queue.rotate(-1)
        index += 1
        my_petrol = 0
        pumps_queue_copy = pumps_queue.copy()
print(index)