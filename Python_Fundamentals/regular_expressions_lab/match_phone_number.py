import re

text = input()

pattern = r"\+359 2 \w{3} \w{4}|\+359-2-\w{3}-\w{4}\b"
regex_pattern = re.compile(pattern)
result = regex_pattern.findall(text)

print(*result, sep= ", ")