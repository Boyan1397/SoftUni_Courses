number_of_lines = int(input())
some_dict = {}

for _ in range(number_of_lines):
    key = input()
    value = input()
    if key not in some_dict:
        some_dict[key] = []
        some_dict[key].append(value)
    else:
        some_dict[key].append(value)
for some_key, some_value in some_dict.items():
    print(f"{some_key} - {some_value}")