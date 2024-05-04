n_students = int(input())
my_dict = {}
for _ in range(n_students):
    student_data = tuple(input().split())
    name, grade = student_data
    if name not in my_dict:
        my_dict[name] = []
    my_dict[name].append(float(grade))

for name, grades in my_dict.items():
    average = sum(grades) / len(grades)
    grades = [f"{el:.2f}" for el in grades]
    print(f"{name} -> {' '.join(grades)} (avg: {average:.2f})")