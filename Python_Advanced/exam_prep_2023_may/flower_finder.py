from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

searched_words = {"rose": "rose",
                  "tulip": "tulip",
                  "lotus": "lotus",
                  "daffodil": "daffodil"
}


found_word = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for key in searched_words.keys():
        searched_words[key] = searched_words[key].replace(vowel, "")
        searched_words[key] = searched_words[key].replace(consonant, "")
        if searched_words[key] == "":
            found_word = True
            print(f"Word found: {key}")
            break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")