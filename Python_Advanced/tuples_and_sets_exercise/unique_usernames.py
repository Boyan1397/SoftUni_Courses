n_lines = int(input())
my_set = set()

for _ in range(n_lines):
    my_set.add(input())

print("\n".join(my_set))