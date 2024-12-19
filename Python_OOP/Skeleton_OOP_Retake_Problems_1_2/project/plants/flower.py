from Python_OOP.Skeleton_OOP_Retake_Problems_1_2.project.plants.base_plant import BasePlant
class Flower(BasePlant):
    def __init__(self, name: str, price: float, water_needed: int, blooming_season: str):
        super().__init__(name, price, water_needed)
        if blooming_season not in ["Spring", "Summer", "Fall", "Winter"]:
            raise ValueError("Blooming season must be a valid one!")
        self.blooming_season = blooming_season

    def plant_details(self):
        return f"Flower: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml, Blooming Season: {self.blooming_season}"
