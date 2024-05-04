my_dict = {}
n_lines = int(input())

for _ in range(n_lines):
    name = input()
    grade = float(input())
    if name not in my_dict.keys():
        my_dict[name] = []
    my_dict[name].append(grade)

for some_name, some_grade in my_dict.items():
    average_grade_per_person = sum(some_grade) / len(some_grade)
    if average_grade_per_person >= 4.50:
        print(f"{some_name} -> {average_grade_per_person:.2f}")


