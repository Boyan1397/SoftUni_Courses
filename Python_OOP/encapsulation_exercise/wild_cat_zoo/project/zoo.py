from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price):

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum(s.salary for s in self.workers)
        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        expenses = sum(s.money_for_care for s in self.animals)
        if self.__budget < expenses:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount:int):
        self.__budget += amount

    def animals_status(self):
        info = {"Lion": [], "Tiger": [], "Cheetah": []}
        [info[an.__class__.__name__].append(str(an)) for an in self.animals]

        result = [
            f"You have {len(self.animals)} animals",

            f"----- {len(info['Lion'])} Lions:",
            *info["Lion"],

            f"----- {len(info['Tiger'])} Tigers:",
            *info["Tiger"],

            f"----- {len(info['Cheetah'])} Cheetahs:",
            *info["Cheetah"],
        ]

        return "\n".join(result)

    def workers_status(self):
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info["Keeper"],

            f"----- {len(info['Caretaker'])} Caretakers:",
            *info["Caretaker"],

            f"----- {len(info['Vet'])} Vets:",
            *info["Vet"],

        ]

        return "\n".join(result)



