from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def get_route_id(self):
        return len(self.routes) + 1

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        curr_user = User(first_name, last_name, driving_license_number)
        self.users.append(curr_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VEHICLE_TYPES.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        curr_vehicle = ManagingApp.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(curr_vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif route.length > length:
                    route.is_locked = True

        curr_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(curr_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        curr_user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        curr_vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        curr_route = [r for r in self.routes if r.route_id == route_id][0]

        if curr_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if curr_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if curr_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        curr_vehicle.drive(curr_route.length)
        if is_accident_happened:
            curr_vehicle.is_damaged = True
            curr_user.decrease_rating()
        else:
            curr_user.increase_rating()

        return str(curr_vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_damaged_vehicles = list(sorted(damaged_vehicles, key=lambda x: (x.brand, x.model)))

        needed_damaged_vehicles = []
        if len(sorted_damaged_vehicles) > count:
            needed_damaged_vehicles = sorted_damaged_vehicles[:count]
        else:
            needed_damaged_vehicles = sorted_damaged_vehicles

        for vehicle in needed_damaged_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(needed_damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = list(sorted(self.users, key=lambda x: -x.rating))

        final = [f"*** E-Drive-Rent ***"]
        for user in sorted_users:
            final.append(str(user))

        return '\n'.join(final)












