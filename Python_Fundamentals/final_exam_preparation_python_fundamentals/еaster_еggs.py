import re

text = input()
#[@#]+[a-z]{3,}[@#]+[^A-Za-z\d]+\/+\d+\/
pattern = r"[@#]+(?P<Paint>[a-z]{3,})[@#]+[^A-Za-z\d]+\/+(?P<Count>\d+)\/+"
results = re.finditer(pattern, text)
for result in results:
    print(f"You found {result.group('Count')} {result.group('Paint')} eggs!")