n = int(input())


def print_parts(size, row):
    print(" " * (size - row), row * "* ")


def upper_part(size):
    for row in range(size):
        print_parts(size, row)


def lower_part(size):
    for row in range(size, 0, -1):
        print_parts(size, row)


def print_rhombus(size):
    upper_part(size)
    lower_part(size)


print_rhombus(n)
