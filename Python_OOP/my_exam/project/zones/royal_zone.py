from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10
    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self) -> str:
        total_battleships = len(self.ships)
        pirate_battleships = sum(1 for ship in self.ships if not isinstance(ship, RoyalBattleship))

        sorted_ships = self.get_ships()
        ship_names = [ship.name for ship in sorted_ships]

        info = []
        info.append("@Royal Zone Statistics@")
        info.append(f"Code: {self.code}; Volume: {self.volume}")
        info.append(
            f"Battleships currently in the Royal Zone: {total_battleships}, {pirate_battleships} out of them are Pirate Battleships.")
        if ship_names:
            info.append(f"#{', '.join(ship_names)}#")

        return '\n'.join(info)