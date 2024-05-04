#finditter
import re

pattern = r">>\b(?P<Furniture>[A-Za-z]+)<<(?P<Price>[\d]+(\.\d+)?)!(?P<Quantity>\d+)\b"
total = 0
my_list = []
while True:
    text = input()
    if text == "Purchase":
        break
    results = re.finditer(pattern, text)
    for result in results:
        my_list.append(result.group("Furniture"))
        total += float(result.group("Price")) * float(result.group("Quantity"))
        print(result.groups())
print("Bought furniture:")
for element in my_list:
    print(element)
print(f"Total money spend: {total:.2f}")

#search
# import re
# pattern = r">>\b(?P<Furniture>[A-Za-z]+)<<(?P<Price>[\d]+(\.\d+)?)!(?P<Quantity>\d+)\b"
# total = 0
# my_list = []
# while True:
#     text = input()
#     if text == "Purchase":
#         break
#     result = re.search(pattern, text)
#     if result:
#         my_list.append(result.group("Furniture"))
#         total += float(result.group("Price")) * int(result.group("Quantity"))
# print("Bought furniture:")
# for element in my_list:
#     print(element)
# print(f"Total money spend: {total:.2f}")
