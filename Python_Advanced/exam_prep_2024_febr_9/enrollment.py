def gather_credits(credit_needed, *args):
    credit_needed = int(credit_needed)
    my_credit = 0
    list_of_courses = []
    args = args

    for course, value in args:
        if my_credit >= credit_needed:
            break

        if course in list_of_courses:
            continue

        list_of_courses.append(course)
        my_credit += value

    if my_credit >= credit_needed:
        return (f"Enrollment finished! Maximum credits: {my_credit}.\nCourses: {', '.join(sorted(list_of_courses))}")

    return f"You need to enroll in more courses! You have to gather {credit_needed - my_credit} credits more."








print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))




print(gather_credits(

60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)

))