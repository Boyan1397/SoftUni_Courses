from math import floor


def center(x1, y1, x2, y2):
    first_absolute = abs(x1) + abs(y1)
    second_absolute = abs(x2) + abs(y2)
    if first_absolute == second_absolute:
        return (f"({floor(x1)}, {floor(y1)})")

    if first_absolute < second_absolute:
        return (f"({floor(x1)}, {floor(y1)})")
    return (f"({floor(x2)}, {floor(y2)})")


first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())
print(center(first_x, first_y, second_x, second_y))