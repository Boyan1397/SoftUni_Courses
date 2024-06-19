from functools import reduce  #когато имаме да пресмятаме незнаем брой числа ползваме reduce
def operate(operator, *args):
    if operator == "+":
        return reduce(lambda a,b: a+b,args)
    elif operator == "-":
        return reduce(lambda a,b: a-b,args)
    elif operator == "*":
        return reduce(lambda a,b: a*b,args)
    else:
        return reduce(lambda a,b: a/b,args)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))