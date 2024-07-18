from collections import deque

tools = deque([int(el) for el in input().split()]) #first
substances = [int(el) for el in input().split()] #last
challenges = [int(el) for el in input().split()]

while tools and substances:
    curr_tool = tools[0]
    curr_subst = substances[-1]
    result = curr_tool * curr_subst
    if result in challenges:
        tools.popleft()
        substances.pop()
        challenges.remove(result)
        if not challenges:
            print("Harry found an ostracon, which is dated to the 6th century BCE.")
            break

    elif result not in challenges:
        tools.popleft()
        curr_tool += 1
        tools.append(curr_tool)

        substances.pop()
        curr_subst -= 1
        if curr_subst > 0:
            substances.append(curr_subst)

if not substances or tools:
    if challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(el) for el in tools)}")
if substances:
    print(f"Substances: {', '.join(str(el) for el in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(el) for el in challenges)}")







