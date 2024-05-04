def palindromes(number):
    if number == number[::-1]:
        return True
    return False


numbers = input().split(", ")
for num in numbers:
    print(palindromes(num))
