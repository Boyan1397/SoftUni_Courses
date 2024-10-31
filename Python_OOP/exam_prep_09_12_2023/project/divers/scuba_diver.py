from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        reduction = round(0.30 * time_to_catch)

        if self.oxygen_level - reduction < 0:
            self.oxygen_level = 0

        else:
            self.oxygen_level -= reduction

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.INITIAL_OXYGEN_LEVEL

