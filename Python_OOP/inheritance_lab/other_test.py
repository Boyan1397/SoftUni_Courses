class Person:
    def __init__(self, name):
        self.name =name

class Student:
    def __init__(self, degree):
        self.degree = degree

class Worker(Person, Student):
    def __init__(self, name, degree, job):
        Person.__init__(self, name)
        Student.__init__(self, degree)
        self.job = job

    def final(self):
        return f"My name is {self.name} and i have studied {self.degree} in SU and now im working as an intern as {self.job}"

lora = Worker("Lora Sladkata", "law", "attourney")
print(lora.final())