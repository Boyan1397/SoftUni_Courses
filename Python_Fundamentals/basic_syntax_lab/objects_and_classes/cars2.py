class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f'The {some_car.make} started')


    def stop(self):
        print(f"The {some_car.make} has stopped")


some_car = Car("Mercedes", "GLE 350 De", 2024)
print(some_car.make)
print(some_car.model)
print(some_car.year)

some_car.start()
some_car.stop()