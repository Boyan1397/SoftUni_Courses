class Some:
    def __init__(self, some_list):
        self.some_list = some_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.some_list)-1:
            raise StopIteration

        self.index += 1
        return self.some_list[self.index]


my_list = Some([1, 2, 4, 5])
for el in my_list:
    print(el)

iterable = Some([1, 3, 5, 23]).__iter__()
while True:
    try:
        print(next(iterable))
    except StopIteration:
        break

# def nums_gen(s_list):
#     for ele in s_list:
#         yield ele * 2
#
# gen = nums_gen([1, 2, 234, 5])
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))