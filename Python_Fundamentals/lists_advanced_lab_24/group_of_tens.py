numbers = [int(s) for s in input().split(", ")]
new_group = []
group = 10
while numbers:
    new_group = [num for num in numbers if num <= group]
    numbers = [el for el in numbers if el not in new_group]
    print(f"Group of {group}'s: {new_group}")
    group += 10
