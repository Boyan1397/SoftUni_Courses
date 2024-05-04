first_input = input().split(" ")
searched_line = input()

all_palindromes = ([element for element in first_input if element[::-1] == element])
found_palindrome = ([searched_line for el in all_palindromes if el == searched_line])
print(all_palindromes)
print(f"Found palindrome {len(found_palindrome)} times")
