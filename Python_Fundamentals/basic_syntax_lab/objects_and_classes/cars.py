class Person:                                                 #class
    def __init__(self, first_name, second_name, some_age =0): #вкараваме parameters  innit
        self.first_name = first_name             #закачаме параметри към instance attributes
        self.second_name = second_name           #закачаме параметри към instance attributes
        self.some_age = some_age                 #закачаме параметри към instance attributes


me = Person("Boyan", "Ivanov", 22)  #object or instance
print(me.first_name)
print(me.second_name)
print(me.some_age)