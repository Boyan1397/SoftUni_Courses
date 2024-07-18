class Car:
    def __init__(self, name, model, engine): #parameters
        self.name = name #instance atributes
        self.model = model #instance atributes
        self.engine = engine #instance atributes

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


car = Car("Kia", "Rio", "1.3L B3 I4") #object
          #arguments

print(car.get_info())