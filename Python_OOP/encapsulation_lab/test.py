class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed #calls the setter method

    def drive(self):
        return f"We are driving with max speed {self.max_speed} kmh"

    @property         #getter method
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter #setter method
    def max_speed(self, value):
        if value > 447:
            value = 447
        self.__max_speed = value  #sets the private attr

s = Car(447)
print(s.max_speed)
print(s.drive())
s.max_speed = 256
print(s.drive())