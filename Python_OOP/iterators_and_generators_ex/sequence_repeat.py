class sequence_repeat:
    def __init__(self, str_sequence, num):
        self.sequence = list(str_sequence)
        self.num = num
        self.max = len(self.sequence)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.num - 1:
            raise StopIteration

        self.index += 1
        return self.sequence[self.index % self.max]




result = sequence_repeat('abc', 5)

for item in result:

    print(item, end ='')