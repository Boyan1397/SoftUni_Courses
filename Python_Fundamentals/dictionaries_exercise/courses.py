my_dict = {}
courses_input = input().split(" : ")
while courses_input[0] != "end":
    course_name, username = courses_input[0], courses_input[1]
    if course_name not in my_dict.keys():
        my_dict[course_name] = []
    my_dict[course_name].append(username)
    courses_input = input().split(" : ")

for course, some_name in my_dict.items():
    print(f"{course}: {len(my_dict[course])}")
    for name in some_name:
        print(f"-- {name}")