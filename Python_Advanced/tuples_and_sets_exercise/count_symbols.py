words = input()

for letter in sorted(set(words)):
    print(f"{letter}: {words.count(letter)} time/s")