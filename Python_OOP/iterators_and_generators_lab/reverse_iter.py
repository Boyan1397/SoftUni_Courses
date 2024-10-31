from typing import List


class reverse_iter:
    def __init__(self, numbers: List):
        self.numbers = numbers
        self.start = -1
                                                           # def __iter__(self):  with intance attr
                                                           #     return reversed(self.numbers)
    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start < len(self.numbers):
            return self.numbers[self.start]

        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:

    print(item)


