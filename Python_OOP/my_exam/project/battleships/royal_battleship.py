from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 100

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMUNITION)

    def attack(self):
        """
        Royal Battleship uses 25 units of ammunition per attack.
        """
        if self.ammunition > 0:
            self.ammunition -= 25
        else:
            self.ammunition = 0