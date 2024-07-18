from collections import deque

textiles = deque([int(el) for el in input().split()]) #first
medicaments = [int(el) for el in input().split()] #last

my_dict = {"Patch": 0, "Bandage": 0, "MedKit": 0}



while True:
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break
    if not textiles:
        print("Textiles are empty.")
        break
    if not medicaments:
        print("Medicaments are empty.")
        break
    textile = textiles[0]
    med = medicaments[-1]
    curr_sum = textile + med
    if curr_sum == 30:
        textiles.popleft()
        medicaments.pop()
        my_dict["Patch"] += 1
    elif curr_sum == 40:
        textiles.popleft()
        medicaments.pop()
        my_dict["Bandage"] += 1
    elif curr_sum == 100:
        textiles.popleft()
        medicaments.pop()
        my_dict["MedKit"] += 1
    elif curr_sum > 100:
        my_dict["MedKit"] += 1
        textiles.popleft()
        medicaments.pop()
        medicaments[-1] += (curr_sum - 100)
    else:
        textiles.popleft()
        medicaments[-1] += 10


sorted_dict = dict(sorted(my_dict.items(), key= lambda x: (-x[1], x[0])))



for name, value in sorted_dict.items():
    if value:
        print(f"{name} - {value} ")

if textiles:
    textiles.reverse()
    print(f"Textiles left: {', '.join(str(el) for el in textiles)}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(el) for el in medicaments)}")