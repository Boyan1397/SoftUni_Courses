n_lines = int(input())
my_set = set()

for _ in range(n_lines):
    for el in input().split():
        my_set.add(el)

print(*my_set, sep="\n")