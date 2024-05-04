def add_lesson(lessons_list, title):
    if title not in lessons_list:
        lessons_list.append(title)
    return lessons_list


def insert_lesson(lessons_list, title, index):
    if title not in lessons_list:
        lessons_list.insert(int(index_or_title), title)
    return lessons_list


def remove_lesson(lessons_list, title):
    if title not in lessons_list:
        lessons_index = lessons_list.index(title)
        if lessons_index + 1 in range(len(lessons_list)):
            if "Exercise" in lessons_list[lessons_index +1]:
                lessons_list.pop(lessons_index +1)
    lessons_list.remove(title)
    return lessons_list


def swap_lesson(lessons_list, first_lesson, second_lesson):
    if first_lesson in lessons_list and second_lesson in lessons_list:
        first_index = lessons_list.index(first_lesson)
        second_index = lessons_list.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_index + 1 in range(len(lessons_list)):
            first_has_exercise = "Exercise" in lessons_list[first_index+ 1]
        if second_index + 1 in range(len(lessons_list)):
            second_has_exercise = "Exercise" in lessons_list[second_index +1]
        lessons_list[first_index], lessons_list[second_index] = lessons_list[second_index], lessons_list[first_index]
        if first_has_exercise and second_has_exercise:
            lessons_list[first_index+1], lessons_list[second_index+1] = lessons_list[second_index+1], lessons_list[first_index+1]
        elif not first_has_exercise and second_has_exercise:
            lessons_list.insert(first_index+1, lessons_list.pop(second_index + 1))
        elif first_has_exercise and not second_has_exercise:
            lessons_list.insert(second_index +1,lessons_list.pop(first_index+1))
    return lessons_list


def exercise(lessons_list, title):
    if title in lessons_list and not f"{title}-Exercise":
        title_index = lessons_list.index(title)
        lessons_list.insert(title_index +1, f"{title}-Exercise" )
    elif title not in lessons_list:
        lessons_list.append(title)
        lessons_list.append(f"{title}-Exercise")
    return lessons_list


lessons = input().split(", ")
command = input()
while command != "course start":
    command = command.split(":")
    action, lesson_title = command[0], command[1]
    if len(command) > 2:
        index_or_title = command[2]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        lessons = insert_lesson(lessons, lesson_title, index_or_title)
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        lessons = swap_lesson(lessons, lesson_title, index_or_title)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)

    command = input()
for index, lesson_name in enumerate(lessons):
    print(f"{index+1}.{lesson_name}")
