number = int(input())
searched_word = input()
full_list = []
redacted_list = list()
for i in range(number):
    current_input = input()
    full_list.append(current_input)
    if searched_word in current_input:
        redacted_list.append(current_input)
print(full_list)
print(redacted_list)