from Python_OOP.Skeleton_OOP_Retake_Problems_1_2.project.clients.regular_client import RegularClient
from Python_OOP.Skeleton_OOP_Retake_Problems_1_2.project.clients.business_client import BusinessClient
from Python_OOP.Skeleton_OOP_Retake_Problems_1_2.project.plants.flower import Flower
from Python_OOP.Skeleton_OOP_Retake_Problems_1_2.project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    def __init__(self):
        self.income = 0.0
        self.plants = []
        self.clients = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int,
                  plant_extra_data: str):
        if plant_type not in ["Flower", "LeafPlant"]:
            raise ValueError("Unknown plant type!")

        if plant_type == "Flower":
            plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
        elif plant_type == "LeafPlant":
            plant = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)

        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in ["RegularClient", "BusinessClient"]:
            raise ValueError("Unknown client type!")

        for client in self.clients:
            if client.phone_number == client_phone_number:
                raise ValueError("This phone number has been used!")

        if client_type == "RegularClient":
            client = RegularClient(client_name, client_phone_number)
        elif client_type == "BusinessClient":
            client = BusinessClient(client_name, client_phone_number)

        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = None
        for c in self.clients:
            if c.phone_number == client_phone_number:
                client = c
                break
        if not client:
            raise ValueError("Client not found!")

        plants_to_sell = [p for p in self.plants if p.name == plant_name]
        if not plants_to_sell:
            raise ValueError("Plants not found!")

        if len(plants_to_sell) < plant_quantity:
            return "Not enough plant quantity."

        plant = plants_to_sell[0]
        price = plant.price * plant_quantity * (1 - client.discount / 100)
        self.income += price
        client.update_total_orders()
        client.update_discount()

        for _ in range(plant_quantity):
            self.plants.remove(plant)

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {price:.2f}"

    def remove_plant(self, plant_name: str):
        plant = None
        for p in self.plants:
            if p.name == plant_name:
                plant = p
                self.plants.remove(p)
                # TODO
                return f"Removed {pla}"
        return "No such plant name."

    def remove_clients(self):
        removed_count = 0
        for client in self.clients[:]:
            if client.total_orders == 0:
                self.clients.remove(client)
                removed_count += 1
        return f"{removed_count} client/s removed."

    def shop_report(self):
        unsold_plants = {}
        for plant in self.plants:
            if plant.name not in unsold_plants:
                unsold_plants[plant.name] = 0
            unsold_plants[plant.name] += 1

        report = f"~Flower Shop Report~\nIncome: {self.income:.2f}\nCount of orders: {sum(c.total_orders for c in self.clients)}\n"
        report += f"~~Unsold plants: {len(self.plants)}~~\n"
        for plant_name, count in sorted(unsold_plants.items(), key=lambda x: (-x[1], x[0])):
            report += f"{plant_name}: {count}\n"

        report += f"~~Clients number: {len(self.clients)}~~\n"
        for client in sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number)):
            report += f"{client.client_details()}\n"

        return report.strip()
