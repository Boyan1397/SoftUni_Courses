first_set = set(int(el) for el in input().split())
second_set = set(int(el) for el in input().split())
n_lines = int(input())
for _ in range(n_lines):
    command = input()

    if "Add First" in command:
        for num in command.split():
            if num.isdigit():
                first_set.add(int(num))
    elif "Add Second" in command:
        for num in command.split():
            if num.isdigit():
                second_set.add(int(num))
    elif "Remove First" in command:
        for num in command.split():
            if num.isdigit():
                first_set.discard(int(num))
    elif "Remove Second" in command:
        for num in command.split():
            if num.isdigit():
                second_set.discard(int(num))
    elif "Check Subset" in command:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*(sorted(first_set)), sep = ", ")
print(*(sorted(second_set)), sep = ", ")