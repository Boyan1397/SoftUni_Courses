n = int(input())
special_word = input()
full_list = []
filtered_list = []
for _ in range(n):
    current_input = input()
    full_list.append(current_input)
    if special_word in current_input:
        filtered_list.append(current_input)
print(full_list)
print(filtered_list)