# import re
#
# text = input()
# pattern = r"\b_([A-Za-z0-9]+)\b"
# # pattern = r"(?<=\b_{1})[A-Za-z0-9]+\b"
#
# matches = re.findall(pattern, text)
# print(",".join(matches))

import re

text = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
results = re.findall(pattern, text)
print(",".join(results))