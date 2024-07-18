class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def __validate(cls, value):
        if value < cls.min_age or value > cls.max_age:
            raise ValueError("Invalid ages")
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__validate(value)
        self.__age = value

class Employee(Person):
    min_age = 16
    max_age = 120

    def __init__(self, name, age):
        super().__init__(name, age)


person = Person("Bobo", 15)
emp = Employee("NIkola", 14)
