from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, FreeDiver.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        reduction = round(0.60 * time_to_catch)

        if self.oxygen_level - reduction < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduction

    def renew_oxy(self):
        self.oxygen_level = FreeDiver.INITIAL_OXYGEN_LEVEL

