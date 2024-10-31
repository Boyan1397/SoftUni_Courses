from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) :
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next(filter(lambda s: s.id == subscription_id, self.subscriptions))

        customer_id = subscription.customer_id
        customer = next(filter(lambda c: c.id == customer_id, self.customers))

        trainer_id = subscription.trainer_id
        trainer = next(filter(lambda t: t.id == trainer_id, self.trainers))

        plan_id = subscription.exercise_id
        plan = next(filter(lambda p: p.id == plan_id, self.plans))

        equipment_id = plan.equipment_id
        equipment = next(filter(lambda e: e.id == equipment_id, self.equipment))

        result = [str(subscription),
                  str(customer),
                  str(trainer),
                  str(equipment),
                  str(plan)
                  ]

        return '\n'.join(result)







