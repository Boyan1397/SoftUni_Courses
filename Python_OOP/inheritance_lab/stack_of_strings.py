from typing import List


class Stack:
    def __init__(self):
        self.data: List = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        removed_element = self.data.pop()
        return removed_element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if not self.data:
            return True
        return False

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"

print(Stack())