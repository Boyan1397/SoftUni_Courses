import re

text = input()
pattern = r"([=/])(?P<Destination>[A-Z][A-Za-z]{2,})\1"
total = 0
my_list = []
results = re.finditer(pattern,text)
for result in results:
    my_list.append(result.group("Destination"))
    total += len(result.group("Destination"))
print(f"Destinations: {', '.join(my_list)}")
print(f"Travel Points: {total}")
