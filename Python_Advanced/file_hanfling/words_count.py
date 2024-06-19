import os
import re

path = os.path.join("resources", "words.txt")

with open(path, "r") as file:   #words.txt
    searched_words_list = [el.lower() for el in file.read().split()]

path = os.path.join("resources", "input.txt")

with open(path, "r") as file:
    text_words = file.read()

count_of_words = {}
for searched_word in searched_words_list:
    pattern = rf"\b{searched_word}\b"
    result = re.findall(pattern, text_words, re.IGNORECASE)
    count_of_words[searched_word] = len(result)

count_of_words = dict(sorted(count_of_words.items(), key= lambda x:-x[1]))
path = os.path.join("resources", "output.txt")
with open(path, "w") as file:
    for key, value in count_of_words.items():
        file.write(f"{key}-{value}\n")