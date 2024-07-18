def softuni_students(*args, **kwargs):
    my_dict = {}
    course_students = {}
    invalid_students = set()

    # Process tuple key-value pairs
    for arg in args:
        course_id, username = arg
        if course_id not in kwargs:
            invalid_students.add(username)
        else:
            course_name = kwargs[course_id]
            course_students[username] = course_name

    sorted_dict = dict(sorted(course_students.items(), key= lambda x: x[0]))
    output = ""
    for name, course in sorted_dict.items():
            output += f"*** A student with the username {name} has successfully finished the course {course}!\n"
    if invalid_students:
        output += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
    return output.strip()



# print(softuni_students(
#     ('id_7', 'Silvester1'),
#     ('id_32', 'Katq21'),
#     ('id_7', 'The programmer'),
#     id_76='Spring Fundamentals',
#     id_7='Spring Advanced',
# ))
#
#
# print(softuni_students(
#     ('id_1', 'Kaloyan9905'),
#     id_1='Python Web Framework',
# ))

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))