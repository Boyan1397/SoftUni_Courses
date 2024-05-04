stack = []

for _ in range(int(input())):
    query_data = [int(x) for x in input().split()]
    if 1 == query_data[0]:
        number = query_data[1]
        stack.append(number)
    elif 2 == query_data[0]:
        if stack:
            stack.pop()
    elif 3 == query_data[0]:
        if stack:
            print(max(stack))
    elif 4 == query_data[0]:
        if stack:
            print(min(stack))

stack.reverse()
print(*stack, sep=", ")