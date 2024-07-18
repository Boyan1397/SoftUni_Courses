def softuni_students(*args, **kwargs):
    my_dict = {}
    invalids = set()
    for some_id, name in args:
        if some_id not in kwargs.keys():
            invalids.add(name)
        else:
            course_name = kwargs[some_id]
            my_dict[name].append(course_name)

    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))

    output = ""
    for key, names in sorted_dict.items():
        for name in names:
            output += f"*** A student with the username {name} has successfully finished the course {key}!\n"
    if invalids:
        output += f"!!! Invalid course students: {', '.join(invalids)}"
    return output.strip()

#
# print(softuni_students(
#     ('id_22', 'Programmingkitten'),
#     ('id_11', 'MitkoTheDark'),
#     ('id_321', 'Bobosa253'),
#     ('id_08', 'KrasimirAtanasov'),
#     ('id_32', 'DaniBG'),
#     id_321='HTML & CSS',
#     id_22='Machine Learning',
#     id_08='JS Advanced',
# ))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))