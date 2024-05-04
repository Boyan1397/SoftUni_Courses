from collections import deque
queue = deque()
clients = input()
while clients != "End":
    if clients == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(clients)
    clients = input()

print(f"{len(queue)} people remaining.")