import re

text = input()
pattern = r"([@#])(?P<First>[A-Za-z]{3,})\1\1(?P<Second>[A-Za-z]{3,})\1"
my_words = []
results = re.findall(pattern, text)
for result in results:
    if result[1] == result[2][::-1]:
        my_words.append(f"{result[1]} <=> {result[2]}")

if len(results) == 0:
    print("No word pairs found!")
else:
    print(f"{len(results)} word pairs found!")
if len(my_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(my_words))