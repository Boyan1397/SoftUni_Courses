from collections import deque

contestant_max = deque([int(el) for el in input().split()]) #first
pies = [int(el) for el in input().split()] #last

while contestant_max and pies:
    curr_contestant = contestant_max[0]
    curr_pie = pies[-1]
    if curr_contestant >= curr_pie:
        curr_contestant -= curr_pie
        pies.pop()
        if curr_contestant <= 0:
            contestant_max.popleft()
        else:
            contestant_max.popleft()
            contestant_max.append(curr_contestant)
    elif curr_contestant < curr_pie:
        curr_pie -= curr_contestant
        contestant_max.popleft()
        if len(pies) == 1:
            pies.pop()
            pies.append(curr_pie)
        else:
            if curr_pie == 1:
                pies.pop()
                pies[-1] += 1
            elif curr_pie > 1:
                pies[-1] = curr_pie
if not pies:
    if contestant_max:
        print("We will have to wait for more pies to be baked!")
        print(f"Contestants left: {', '.join(str(el) for el  in contestant_max)}")
    else:
        print("We have a champion!")
if not contestant_max:
    if pies:
        print("Our contestants need to rest!")
        print(f"Pies left: {', '.join(str(el) for el  in pies)}")








