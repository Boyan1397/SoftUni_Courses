from abc import ABC, abstractmethod


class BasePlant(ABC):
    def __init__(self, name: str, price: float, water_needed: int):
        if not name.strip():
            raise ValueError("Plant name cannot be null or empty!")
        if price <= 0.0:
            raise ValueError("Price must be greater than zero!")
        if not (1 <= water_needed <= 2000):
            raise ValueError("Water needed must be between 1 and 2000 ml!")

        self.name = name
        self.price = price
        self.water_needed = water_needed

    @abstractmethod
    def plant_details(self):
        pass
