import math
from collections import deque
from math import floor

expression = deque(input().split())
index = 0

while len(expression) > 1:
    element = expression[index]
    if element == "*":
        for _ in range(index-1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == "/":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif element == "+":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
    elif element == "-":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))

    if expression[1] in "*/+-":
        del expression[1]
        index = 1
    index += 1

print(math.floor(expression[0]))

# 2!!!
# import math
# from collections import deque
# from math import floor
#
# expression = deque(input().split())
# index = 0
#
# while len(expression) > 1:
#     element = expression[index]
#     if expression[index] in "*/+-":
#         for _ in range(index-1):
#             expression.appendleft(eval(f"{expression.popleft()}{element}{expression.popleft()}"))
#
#     if expression[1] in "*/+-":
#         del expression[1]
#         index = 1
#     index += 1
#
# print(math.floor(expression[0]))
