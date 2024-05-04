n_lines = int(input())
longest_inter = set()
for _ in range(n_lines):
    first_data, second_data = [el.split(',') for el in input().split("-")]
    first_set = set(range(int(first_data[0]), int(first_data[1])+ 1))
    second_set = set(range(int(second_data[0]), int(second_data[1])+ 1))

    current_inter = first_set.intersection(second_set)
    if len(current_inter) > len(longest_inter):
        longest_inter = current_inter

print(f"Longest intersection is [{', '.join(str(el) for el in longest_inter)}] with length {len(longest_inter)}")