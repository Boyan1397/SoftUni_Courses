to_be_sorted = ([element for element in input().split(", ")])
sorted_list = sorted(to_be_sorted, key=lambda element: (-len(element), element))
print(sorted_list)


