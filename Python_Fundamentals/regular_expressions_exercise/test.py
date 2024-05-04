import re

text = "My name is 4lora"
result = re.sub(r'\dlora',"bobo", text)
print(result)