import re

text = input()
pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}"

result = re.findall(pattern, text)
print(*result, sep= ", ")


#Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett