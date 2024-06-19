from collections import deque
substrings = deque(input().split())

colors = ["red", "yellow", "blue","orange", "purple", "green"]
combinations = {"orange": ["red", "yellow"],
                "purple": ["red", "blue"],
                "green": ["yellow", "blue"],
}
final = []

while substrings:
    if len(substrings) == 1:
        some_string = substrings.pop()
        if some_string in colors:
            final.append(some_string)
            break
        else:
            break
    if len(substrings) > 1:
        first = substrings.popleft()
        last = substrings.pop()
        if first + last in colors:
            final.append(first + last)
        elif last + first in colors:
            final.append(last + first)
        else:
            middle = len(substrings) // 2
            if len(first) > 1:
                substrings.insert(middle, first[:-1])
            if len(last) > 1:
                substrings.insert(middle, last[:-1])


for element in final:
    if element in combinations.keys():
        for color in combinations[element]:
            if color not in final:
                final.remove(element)
print(final)