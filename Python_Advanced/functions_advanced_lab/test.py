def count_nums(a, b ,*args): #*args  винаги прави tuple  от всички дадени аргументи и ги подава на функцията
    total = a + b            #може да има и отделни аргументи които винаги трябва да са там иначе ще crashne
    for el in args:
        total += el
    return total

print(count_nums(1, 4, 5)) #argument

def some_func(**kwargs): # **kwargs  винаги прави dictionary от всички дадени аргументи и ги подава на функцията
    for key, value in kwargs.items():
        print(f"Her name is {key} and her age is {value}")

some_func(Gogo= 14  ,George= 21 )
some_func(a= "b", r = "o")

def some(a, b, c):
    print(a,b,c)

nums = [1, 2, 3]
some(*nums)

def haha(name, age, town):
    print(f"My age is {age} and my name is {name} from {town}!")

person = {"age": 12, "name": "Bobo", "town": "Haskowo"}
haha(**person)