import re

text = input()
searched_text = input()
pattern = rf"\b{searched_text}\b"
result = re.findall(pattern, text,re.IGNORECASE)
print(len(result))
