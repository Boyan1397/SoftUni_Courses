happiness = [int(el) for el in input().split(" ")]
employees = int(input())
multiplied = [num*employees for num in happiness]
average = sum(multiplied) // len(multiplied)
happy_workers = [empl for empl in multiplied if empl > average]
not_happy = [e for e in multiplied if e <= average]

if len(happy_workers) >= len(not_happy):
    print(f"Score: {len(happy_workers)}/{len(multiplied)}. Employees are happy!")
elif len(happy_workers) < len(not_happy):
    print(f"Score: {len(happy_workers)}/{len(multiplied)}. Employees are not happy!")