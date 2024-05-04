locations = int(input())


for location in range(locations):
    expected_gold_for_day = float(input())
    days = int(input())

    total_gold = 0

    for day in range(days):
        current_gold = float(input())
        total_gold += current_gold

    average = total_gold / days

    if average >= expected_gold_for_day:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        print(f"You need {(expected_gold_for_day - average):.2f} gold.")