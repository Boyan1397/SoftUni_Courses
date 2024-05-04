words = input().split()
palindrome_input = input()
palindromes = [word for word in words if word == word[::-1]]
palindromes_count = [el for el in palindromes if el == palindrome_input]
print(palindromes)
print(f"Found palindrome {len(palindromes_count)} times")