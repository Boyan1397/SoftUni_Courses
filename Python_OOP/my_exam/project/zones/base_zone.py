from abc import ABC, abstractmethod
from typing import List
from project.battleships.base_battleship import BaseBattleship  # Ensure you have this import


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code  # Triggers the setter for validation
        self.volume = volume
        self.ships: List[BaseBattleship] = []  # Initialize ships as an empty list

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self) -> List[BaseBattleship]:
        """
        Returns a list of all battleships in the zone,
        ordered by hit strength descending, then by name ascending.
        """
        return sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))

    @abstractmethod
    def zone_info(self) -> str:
        """
        Returns detailed information about the zone.
        To be implemented by subclasses.
        """
        pass