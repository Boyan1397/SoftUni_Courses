class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    amount = int(input())
    if amount < 0:
        raise ValueCannotBeNegative()

