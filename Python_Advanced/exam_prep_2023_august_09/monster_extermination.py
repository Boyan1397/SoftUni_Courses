from collections import deque

monster_armor = deque([int(el) for el in input().split(",")]) #first
soldier_impact = [int(el) for el in input().split(",")] #last

max_monsters = len(monster_armor)
killed_monsters = 0

while monster_armor and soldier_impact:
    curr_armor = monster_armor[0]
    curr_impact = soldier_impact[-1]
    if curr_impact >= curr_armor:
        killed_monsters += 1
        monster_armor.popleft()
        curr_impact -= curr_armor
        if curr_impact > 0:
            if len(soldier_impact) > 1:
                soldier_impact.pop()
                soldier_impact[-1] += curr_impact
            elif len(soldier_impact) == 1:
                soldier_impact[-1] = curr_impact
        else:
            soldier_impact.pop()

    elif curr_impact < curr_armor:
        soldier_impact.pop()
        curr_armor -= curr_impact
        monster_armor.popleft()
        monster_armor.append(curr_armor)


if killed_monsters == max_monsters:
    print("All monsters have been killed!")

if not soldier_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")



