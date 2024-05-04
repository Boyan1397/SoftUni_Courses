my_input = (input())
stack = []
for index in range(len(my_input)):
    if my_input[index] == "(":
        stack.append(index)
    elif my_input[index] == ")":
        start_index = stack.pop()
        end_index = index
        print(my_input[start_index:end_index+1])