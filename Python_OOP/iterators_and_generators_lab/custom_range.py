class custom_range:
    def __init__(self,name, start, end):
        self.name= name
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        count = self.start
        if self.start < self.end + 1:
            self.start += 1
            return count

        raise StopIteration

one_to_ten = custom_range("gogo", 1, 10)

for num in one_to_ten.name:

    print(num)


# iterator = one_to_ten.__iter__()   while loop
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break