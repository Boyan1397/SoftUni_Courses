n_lines = int(input())
even_set = set()
odd_set = set()

for line in range(1,n_lines+1):
    name = input()
    current_sum = 0
    for letter in name:
        current_sum += ord(letter)

    final_sum = current_sum // line
    if final_sum % 2 == 0:
        even_set.add(final_sum)
    else:
        odd_set.add(final_sum)

if sum(odd_set) == sum(even_set):
    print(*(odd_set.union(even_set)), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*(odd_set.difference(even_set)), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*(odd_set.symmetric_difference(even_set)), sep=", ")