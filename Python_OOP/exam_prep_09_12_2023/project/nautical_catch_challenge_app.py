from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in NauticalCatchChallengeApp.DIVER_TYPES.keys():
            return f"{diver_type} is not allowed in our competition."

        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
            return f"{diver_name} is already a participant."
        except IndexError:
            current_diver = NauticalCatchChallengeApp.DIVER_TYPES[diver_type](diver_name)
            self.divers.append(current_diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in NauticalCatchChallengeApp.FISH_TYPES.keys():
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            fish = [f for f in self.fish_list if f.name == fish_name][0]
            return f"{fish_name} is already permitted."
        except IndexError:
            current_fish = NauticalCatchChallengeApp.FISH_TYPES[fish_type](fish_name, points)
            self.fish_list.append(current_fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
        except IndexError:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = [f for f in self.fish_list if f.name == fish_name][0]
        except IndexError:
            return f"The {fish_name} is not allowed to be caught in this competition."

        diver = [d for d in self.divers if d.name == diver_name][0]
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        fish = [f for f in self.fish_list if f.name == fish_name][0]
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level <= 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level <= 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level <= 0:
                diver.has_health_issue = True
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_with_issues = [d for d in self.divers if d.has_health_issue]

        for diver in divers_with_issues:
            diver.has_health_issue = False
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_with_issues)}"

    def diver_catch_report(self, diver_name: str) -> str:
        diver = next((d for d in self.divers if d.name == diver_name), None)

        report = f"**{diver_name} Catch Report**\n"
        report += "\n".join(fish.fish_details() for fish in diver.catch)

        return report.strip()

    def competition_statistics(self) -> str:
        healthy_divers = [d for d in self.divers if not d.has_health_issue]

        sorted_divers = sorted(
            healthy_divers,
            key=lambda d: (-d.competition_points, -len(d.catch), d.name)
        )

        report = "**Nautical Catch Challenge Statistics**\n"
        report += "\n".join(str(diver) for diver in sorted_divers)

        return report.strip()



















