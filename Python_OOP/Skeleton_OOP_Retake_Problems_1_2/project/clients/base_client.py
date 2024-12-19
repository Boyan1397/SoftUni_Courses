from abc import ABC


class BaseClient(ABC):
    def __init__(self, name: str, phone_number: str):
        if len(name.strip()) < 2:
            raise ValueError("Name must be at least two characters long!")
        if not phone_number.isdigit():
            raise ValueError("Phone number can contain only digits!")

        self.name = name
        self.phone_number = phone_number
        self.discount = 0.0
        self.total_orders = 0

    def update_total_orders(self):
        self.total_orders += 1

    def client_details(self):
        return f"Client: {self.name}, Phone number: {self.phone_number}, Orders count: {self.total_orders}, Discount: {int(self.discount)}%"
