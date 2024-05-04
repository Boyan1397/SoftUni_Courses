#every object has its:
#name
#characteristics
#actions it can do

#classes == templates for the objects
#чертеж за създаване на object
#всеки клас има свои свобствени абстрактни-начални характеристики
#всеки клас им свои методи
class Bottle: #davame ime na klas
    def __init__(self, ml, brand, color): #дефинираме магическа функия  #параметри self  и още каквито му подадем
        self.ml = ml   #след селф задаваме и след това обяваваме че ще получи нещо
        self.brand = brand
        self.color = color
    def exploded(self):
        print("grumna")

bottle1 = Bottle(500, "devin", "blue")
print(bottle1.ml)
print(bottle1.brand)
print(bottle1.color)
bottle1.exploded()
