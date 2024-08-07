from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name:str, mana_cost: int):
        if skill_name in self.skills.keys():
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        output = ""
        output += f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\n"\
                  f"MP: {self.mp}\n"
        for name, mana in self.skills.items():
            output += f"==={name} - {mana}\n"

        return output


player = Player("George", 50, 100)
