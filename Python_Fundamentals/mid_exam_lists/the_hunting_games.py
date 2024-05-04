days_of_adventure = int(input())
number_of_players = int(input())
groups_energy = float(input())
water_per_person_per_day = float(input())
food_per_person_per_day = float(input())
energy_losses = list(map(float, input().split()))

water_to_have = days_of_adventure * water_per_person_per_day * number_of_players
food_to_have = days_of_adventure * food_per_person_per_day * number_of_players
for day in range(1, days_of_adventure + 1):
    groups_energy -= energy_losses[day - 1]
    if 0 >= groups_energy:
        print(f"You will run out of energy. You will be left with {food_to_have:.2f} food and {water_to_have:.2f} water.")
        break
    if day % 2 == 0:
        water_to_drink = 0.3 * water_to_have
        groups_energy *= 1.05
        water_to_have -= water_to_drink
    if day % 3 == 0:
        food_to_eat = food_to_have / number_of_players
        groups_energy *= 1.10
        food_to_have -= food_to_eat * number_of_players
    if groups_energy > 0:
        print(f"You are ready for the quest. You will be left with {groups_energy:.2f} energy!")