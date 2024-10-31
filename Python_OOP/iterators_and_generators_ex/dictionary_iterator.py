from typing import Dict

class dictionary_iter:
    def __init__(self, some_dict: Dict):
        self.some_dict = some_dict
        self.list_of_dict = list(self.some_dict.items())
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.some_dict.keys()) - 1:
            raise StopIteration

        self.start += 1
        return self.list_of_dict[self.start]


# class dictionary_iter:
#     def __init__(self, some_dict: Dict):
#         self.some_dict = some_dict.items()
# 
#
#     def __iter__(self):
#         return iter(self.some_dict)

result = dictionary_iter({1: "1", 2: "2"})

for x in result:

    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})

for x in result:
    print(x)