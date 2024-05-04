class Circle:
    __pi = 3.14  #class attribute

    def __init__(self, diameter):    #konstruktor
        self.diameter = diameter     #intance attribute

    def calculate_circumference(self):    #method
        return self.diameter * self.__pi  #vinagi rabotim sus #self v methods

    def calculate_area(self):              #method
        return self.__pi * (self.diameter / 2) ** 2

    def calculate_area_of_sector(self, angle):     #method
        return (angle / 360) * self.__pi * (self.diameter / 2) ** 2


circle = Circle(10)     #davame stoinost na harakteristikata na obekta
angle = 5
print(f'{circle.calculate_circumference():.2f}')
print(f'{circle.calculate_area():.2f}')
print(f'{circle.calculate_area_of_sector(angle):.2f}')

