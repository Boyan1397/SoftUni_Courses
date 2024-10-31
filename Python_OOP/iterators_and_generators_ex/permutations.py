from itertools import permutations
def possible_permutations(some_list):
    for el in permutations(some_list):
        yield [*el]

[print(n) for n in possible_permutations([1, 2, 3])]
