from typing import List

from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    VALID_ZONES = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}
    VALID_SHIPS= {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}

    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.VALID_ZONES.keys():
            raise Exception("Invalid zone type!")

        for zone in self.zones:
            if zone.code == zone_code:
                raise Exception("Zone already exists!")

        my_zone = BattleManager.VALID_ZONES[zone_type](zone_code)
        self.zones.append(my_zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.VALID_SHIPS.keys():
            raise Exception(f"{ship_type} is an invalid type of ship!")

        my_ship = BattleManager.VALID_SHIPS[ship_type](name, health, hit_strength)
        self.ships.append(my_ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"
        if not ship.health > 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if isinstance(ship, RoyalBattleship) and isinstance(zone, PirateZone):
            ship.is_attacking = True
        elif isinstance(ship, PirateBattleship) and isinstance(zone, RoyalZone):
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        my_ship = next((s for s in self.ships if s.name == ship_name), None)
        if my_ship is None:
            return "No ship with this name!"

        if not my_ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(my_ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attackers = [s for s in zone.ships if s.is_attacking]
        targets = [s for s in zone.ships if not s.is_attacking]

        if len(attackers) == 0 or len(targets) == 0:
            return "Not enough participants. The battle is canceled."

        attacker = max(attackers, key=lambda s: s.hit_strength)
        target = min(targets, key=lambda s: s.health)

        attacker.attack()
        target.take_damage(attacker)

        if target.health == 1:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."

        if attacker.ammunition == 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."
    def get_statistics(self):
        # Step 1: Collect available battleships
        available_ships = [ship for ship in self.ships if ship.is_available]
        available_ship_names = [f"#RoyalOne#" for ship in available_ships]
        available_ships_count = len(available_ships)

        # Step 2: Collect zone statistics
        sorted_zones = sorted(self.zones, key=lambda z: z.code)
        zone_statistics = []
        for zone in sorted_zones:
            zone_info = zone.zone_info()
            zone_statistics.append(zone_info)

        # Step 3: Format the statistics
        result = []

        if available_ships_count > 0:
            result.append(f"Available Battleships: {available_ships_count}")
            result.append(", ".join(available_ship_names))
        else:
            result.append("Available Battleships: 0")

        result.append("\n***Zones Statistics:***")
        result.append(f"Total Zones: {len(sorted_zones)}")
        result.extend(zone_statistics)

        return "\n".join(result)