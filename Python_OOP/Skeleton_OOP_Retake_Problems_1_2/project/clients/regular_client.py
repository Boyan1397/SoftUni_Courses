from Python_OOP.Skeleton_OOP_Retake_Problems_1_2.project.clients.base_client import BaseClient

class RegularClient(BaseClient):
    def __init__(self, name: str, phone_number: str):
        super().__init__(name, phone_number)

    def update_discount(self):
        if self.total_orders > 0:
            self.discount = 5.0
