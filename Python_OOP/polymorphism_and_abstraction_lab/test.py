class Cat:
    def __init__(self, name, weigth):
        self.name = name
        self.weigth = weigth

class Person:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __len__(self):
        return len(self.name)   #we can return whatever we want from the instance methods

    def __add__(self, other):
        return f"{self.name} and {other.name}"

    def __lt__(self, other):
        return self.size > other.size




p = Person("Boyan", 81)
p2 = Person("Nikola", 91)
c = Cat("Minka", 8)

print(len(p))
print(p + p2) #the + triggers the __add__method OF THE LEFT ONE
print(p + c)
# print(c + p) cannot do that cause its defined in the Person class
print(p.__add__(p2)) #same thing as the upper one
print(p > p2)