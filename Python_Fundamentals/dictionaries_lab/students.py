students_list = input().split(":")
courses_dict = {}
while len(students_list) > 1:
    name, ID, course = students_list[0], students_list[1], students_list[2]
    if course not in courses_dict:
        courses_dict[course] = {name: ID}
    else:
        courses_dict[course][name] = ID
    students_list = input().split(":")

wanted_course = students_list[0].replace("_", " ")
for key, value in courses_dict[wanted_course].items():
    print(f"{key} - {value}")
print(courses_dict)