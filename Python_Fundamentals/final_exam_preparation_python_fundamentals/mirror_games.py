import re

text = input()
pattern = r"([@#])(?P<First>[A-Za-z]{3,})\1\1(?P<Second>[A-Za-z]{3,})\1"
valids_count = 0
my_words = []
results = re.finditer(pattern, text)
for result in results:
    if result.group("First") == result.group("Second")[::-1]:
        my_words.append(f"{result.group('First')} <=> {result.group('Second')}")
    valids_count += 1

if valids_count == 0:
    print("No word pairs found!")
else:
    print(f"{valids_count} word pairs found!")

if len(my_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(f"{', '.join(my_words)}")
