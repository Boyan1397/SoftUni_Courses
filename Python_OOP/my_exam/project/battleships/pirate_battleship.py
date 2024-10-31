from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 80

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMUNITION)

    def attack(self):
        """
        Pirate Battleship uses 10 units of ammunition per attack.
        """
        if self.ammunition > 0:
            self.ammunition -= 10
        else:
            self.ammunition = 0
