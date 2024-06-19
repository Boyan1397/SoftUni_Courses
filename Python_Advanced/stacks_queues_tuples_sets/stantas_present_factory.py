from collections import deque

materials_values = [int(el) for el in input().split()]
magic_level_values = deque(int(el) for el in input().split())

toys_crafting = {150: "Doll",250: "Wooden train", 300: "Teddy bear" ,400: "Bicycle"}
final = []

while materials_values and magic_level_values:
    material = materials_values.pop()
    magic = magic_level_values.popleft()
    if material == 0 and magic == 0:
        continue
    if material == 0:
        magic_level_values.appendleft(magic)
        continue
    if magic == 0:
        materials_values.append(material)
        continue
    crafted_value = material * magic
    if crafted_value < 0:
        materials_values.append(material + magic)
    elif crafted_value in toys_crafting.keys():
        final.append(toys_crafting[crafted_value])
    else:
        materials_values.append(material + 15)

if "Doll" in final and "Wooden train" in final or "Bicycle" in final and "Teddy bear" in final:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_values:
    print(f"Materials left: {', '.join(str(el) for el in reversed(materials_values))}")
if magic_level_values:
    print(f"Magic left: {', '.join(str(el) for el in magic_level_values)}")

for el in sorted(set(final)):
    print(f"{el}: {final.count(el)}")
