import re

text = input()
pattern = r"(?P<Day>\d{2})(?P<Separator>[\-\.\/])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})"

matches = re.finditer(pattern, text)
for match in matches:
    print(f"Day: {match.group('Day')}, Month: {match.group('Month')}, Year: {match.group('Year')}")