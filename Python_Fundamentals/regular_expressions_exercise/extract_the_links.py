# findall
# import re
#
# text = input()
# pattern = r"\w{3}\.[A-Za-z\d\-]+\.[a-z\.]+"
# while text:
#     results = re.findall(pattern, text)
#     if results:
#         print(results[0])
#     text = input()

# search
import re
import re
my_list = []
text = input()
pattern = r"\w{3}\.[A-Za-z\d\-]+\.[a-z\.]+"
while text:
    results = re.search(pattern, text)
    if results:
        my_list.append(results.group())
    text = input()

for element in my_list:
    print(element)
