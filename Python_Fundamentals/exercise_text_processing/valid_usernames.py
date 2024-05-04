def is_redundant(some_name):
    if " " not in some_name:
        return True
    return False


def is_character_valid(some_name):
    if some_name.isalnum() or "-" in some_name or "_" in some_name:
        return True
    return False


def is_length_valid(some_name):
    if 3 < len(some_name) <= 16:
        return True
    return False


def is_valid(some_name):
    if is_length_valid(some_name) and is_character_valid(some_name) and is_redundant(some_name):
        return True


names = input().split(", ")
for name in names:
    if is_valid(name):
        print(name)