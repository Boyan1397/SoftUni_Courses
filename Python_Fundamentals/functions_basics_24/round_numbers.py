def round_nums():
    float_nums = [float(el) for el in input().split()]
    rounded = [round(num) for num in float_nums]
    return rounded
print(round_nums())