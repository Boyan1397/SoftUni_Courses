text = input().split()
new_list = []
for el in text:
    if len(el) % 2 == 0:
        new_list.append(el)
result = "\n".join(new_list)
print(result)
