import re

text = input()
pattern = r"\s([a-z][a-z0-9\.\-\_]+)@[a-z][a-z\-]+\.[a-z\.?]+\b"
result = re.finditer(pattern, text)
for element in result:
    print(element.group())