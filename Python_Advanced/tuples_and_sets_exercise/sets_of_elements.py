data = (int(el) for el in input().split())
n, m = data

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

print("\n".join(first_set.intersection(second_set)))