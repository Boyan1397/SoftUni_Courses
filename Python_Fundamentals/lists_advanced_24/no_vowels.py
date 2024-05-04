some_name = input()
vowels = ['a', 'o', 'u', 'e', 'i']
no_vowels = [el for el in some_name if el.lower() not in vowels]
print("".join(no_vowels))