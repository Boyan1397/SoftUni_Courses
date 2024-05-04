import math

nums = ([int(number) for number in input().split(" ")])
factor = int(input())

happiness = [element*factor for element in nums]
average = sum(happiness) / len(happiness)

happy_workers = ([worker for worker in happiness if worker >= average])
sad_workers = ([worker for worker in happiness if worker <= average])

happy_message = "Employees are happy!"
sad_message = "Employees are not happy!"
if len(sad_workers) >= len(happiness) / 2:
    print(f"Score: {len(happy_workers)}/{len(happiness)}. {sad_message}")
else:
    print(f"Score: {len(happy_workers)}/{len(happiness)}. {happy_message}")

