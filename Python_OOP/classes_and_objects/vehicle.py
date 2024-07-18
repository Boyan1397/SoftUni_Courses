class Vehicle:
    def __init__(self, mileage, max_speed=150): #optional
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)

new = Vehicle(50, 440)
print(new.mileage)
print(new.max_speed)
print(new.__dict__)