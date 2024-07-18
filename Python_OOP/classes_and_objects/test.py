class Laptop:
    def __init__(self, brand, model, age): #state
        self.brand = brand
        self.model = model
        self.age = age

    def get_info(self):              #interface
        return self.brand + " " + self.model

    def __repr__(self):
        return f"this is {self.brand} of {self.model} and is {self.age} yrs old"
    #
    # def __str__(self):
    #     return self.brand + " " + self.model + self.age

msi = Laptop("MSI COMPANY", "bravo15", "5")
print((msi))