import math
import re

text = input()
pattern = r"([\#\|])(?P<Product>[A-Za-z\s]+)\1(?P<Date>\d{2}\/\d{2}\/\d{2})\1(?P<Calories>\d+)\1"
total_calories = 0
results = re.finditer(pattern,text)
for result in results:
    total_calories += int(result.group("Calories"))
print(f"You have food to last you for: {math.floor(total_calories / 2000)} days!")
final_results = re.finditer(pattern, text)
for final_result in final_results:
    print(f"Item: {final_result.group('Product')}, Best before: {final_result.group('Date')}, Nutrition: {final_result.group('Calories')}")