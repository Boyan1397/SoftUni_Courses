#1
# command = input()
# my_dict = {}
# list_with_elements = []
# while command != "stop":
#     list_with_elements.append(command)
#     command = input()
#
# for index in range(0, len(list_with_elements), 2):
#     resource = list_with_elements[index]
#     quantity = int(list_with_elements[index + 1])
#     if resource not in my_dict.keys():
#         my_dict[resource] = quantity
#     else:
#         my_dict[resource] += quantity
# for resource_name, my_quantity in my_dict.items():
#     print(f"{resource_name} -> {my_quantity}")
#2
my_dict = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in my_dict:
        my_dict[resource] = quantity
    else:
        my_dict[resource] += quantity
for resource_name, my_quantity in my_dict.items():
     print(f"{resource_name} -> {my_quantity}")
