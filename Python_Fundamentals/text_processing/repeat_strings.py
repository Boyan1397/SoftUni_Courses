my_strings = input().split()
result = ""
for element in my_strings:
    result += (element*len(element))
print(result)