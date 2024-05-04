     #key  #a = argument
#x = lambda a: print(a) #print(a) = expresion
#x(43245235) #and call it

y = lambda a, b:a * b
print(y(4, 3))

z = lambda c, d: (c * d) ** 3
print(z(4, 5))

def my_func(n):
    return lambda b: b * n
my_first = my_func(4)
print(my_first(5))