from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8
    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self) -> str:
        total_battleships = len(self.ships)
        royal_battleships = sum(1 for ship in self.ships if isinstance(ship, RoyalBattleship))

        sorted_ships = self.get_ships()
        ship_names = [ship.name for ship in sorted_ships]

        info = []
        info.append("@Pirate Zone Statistics@")
        info.append(f"Code: {self.code}; Volume: {self.volume}")
        info.append(
            f"Battleships currently in the Pirate Zone: {total_battleships}, {royal_battleships} out of them are Royal Battleships.")
        if ship_names:
            info.append(f"#{', '.join(ship_names)}#")

        return '\n'.join(info)