from collections import deque

worms = [int(el) for el in input().split()] #last
holes = deque([int(el) for el in input().split()]) #first
max_worms = len(worms)
matches = 0

while worms and holes:
    curr_worm = worms[-1]
    curr_hole = holes[0]
    if curr_hole == curr_worm:
        worms.pop()
        holes.popleft()
        matches += 1
    else:
        curr_worm = curr_worm - 3
        holes.popleft()
        worms.pop()
        worms.append(curr_worm)
        if curr_worm <= 0:
            worms.pop()

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    if matches == max_worms:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")

else:
    print(f"Worms left: {', '.join([str(el) for el in worms])}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(el) for el in holes])}")