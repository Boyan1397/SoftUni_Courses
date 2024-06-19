def age_assignment(*args, **kwargs):
    final = {}
    for name in args:
        for letter, value in kwargs.items():
            if name[0] == letter:
                final[name] = value
    final = sorted(final.items(), key= lambda kvp: kvp)
    return "\n".join([f"{name} is {val} years old." for name, val in final])


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))