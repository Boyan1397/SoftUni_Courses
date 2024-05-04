number_of_lines = int(input())
total_result = 0
for number in range(1,number_of_lines +1):
    letter = input()
    total_result += ord(letter)
print(f"The sum equals: {total_result}")