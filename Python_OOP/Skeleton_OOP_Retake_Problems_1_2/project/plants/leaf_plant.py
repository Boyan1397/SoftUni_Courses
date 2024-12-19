from Python_OOP.Skeleton_OOP_Retake_Problems_1_2.project.plants.base_plant import BasePlant

class LeafPlant(BasePlant):
    def __init__(self, name: str, price: float, water_needed: int, size: str):
        super().__init__(name, price, water_needed)
        if size not in ["S", "M", "L"]:
            raise ValueError("Size must be a valid one!")
        self.size = size

    def plant_details(self):
        return f"Leaf Plant: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml, Size: {self.size}"
