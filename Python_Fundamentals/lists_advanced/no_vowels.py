vowels = ['a', 'o', 'u', 'e', 'i']
word = input()
print("".join(element for element in word if element.lower() not in vowels))
