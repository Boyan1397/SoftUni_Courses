from collections import deque

elf_energy = deque([int(el) for el in input().split()])
materials_boxes = [int(el) for el in input().split()]

total_energy = 0
toys_made = 0
counter = 0


while elf_energy and materials_boxes:
    current_elv_en = elf_energy.popleft()
    material = materials_boxes[-1]

    if current_elv_en < 5:
        continue
    counter += 1
    current_toys_count = 0

    if counter % 3 == 0:
        material *= 2
        current_toys_count += 1

    if current_elv_en >= material:
        materials_boxes.pop()
        total_energy += material
        current_elv_en -= material
        if counter % 5 != 0:
            current_toys_count += 1
            current_elv_en += 1
        else:
            current_toys_count = 0
    else:
        current_elv_en *= 2
        current_toys_count = 0


    toys_made += current_toys_count
    elf_energy.append(current_elv_en)

print(f"Toys: {toys_made}")
print(f"Energy: {total_energy}")

if elf_energy:
    print(f"Elves left: {', '.join(str(el) for el in elf_energy)}")
if materials_boxes:
    print(f"Boxes left: {', '.join(str(el) for el in materials_boxes)}")

