# first = ord(input())
# second = ord(input())
# my_chars = (input())
# print(sum((ord(element)) for element in my_chars if first < ord(element) < second))

first = ord(input())
second = ord(input())
my_chars = (input())
total = 0
for element in my_chars:
    if first < ord(element) < second:
        total += ord(element)
print(total)
