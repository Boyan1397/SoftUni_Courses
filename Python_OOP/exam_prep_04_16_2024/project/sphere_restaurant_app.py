from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    WAITER_TYPES = {"HalfTimeWaiter": HalfTimeWaiter, "FullTimeWaiter": FullTimeWaiter}
    CLIENT_TYPES = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.WAITER_TYPES.keys():
            return f"{waiter_type} is not a recognized waiter type."

        for waiter in self.waiters:
            if waiter_name == waiter.name:
                return f"{waiter_name} is already on the staff."

        current_waiter = SphereRestaurantApp.WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append(current_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENT_TYPES.keys():
            return f"{client_type} is not a recognized client type."

        for client in self.clients:
            if client_name == client.name:
                return f"{client_name} is already a client."

        current_client = SphereRestaurantApp.CLIENT_TYPES[client_type](client_name)
        self.clients.append(current_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        try:
            waiter = [w for w in self.waiters if w.name == waiter_name][0]
            return waiter.report_shift()
        except IndexError:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            client = [c for c in self.clients if c.name == client_name][0]
            return f"{client_name} earned {client.earning_points(order_amount)} points from the order."
        except IndexError:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        try:
            client = [c for c in self.clients if c.name == client_name][0]
            return f"{client_name} received a {client.apply_discount()[0]}% discount. Remaining points {client.apply_discount()[1]}"
        except IndexError:
            return f"{client_name} cannot get a discount because this client is not admitted!"


    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)

        # Get detailed information for each waiter
        waiter_info = "** Waiter Details **\n"
        for waiter in sorted_waiters:
            waiter_info += str(waiter) + "\n"

        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        total_client_points = sum(client.points for client in self.clients)
        total_clients = len(self.clients)

        report = f"$$ Monthly Report $$\n"
        report += f"Total Earnings: ${total_earnings:.2f}\n"
        report += f"Total Clients Unused Points: {total_client_points}\n"
        report += f"Total Clients Count: {total_clients}\n"
        report += waiter_info

        return report.strip()