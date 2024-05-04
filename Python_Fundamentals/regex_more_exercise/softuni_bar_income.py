import re

pattern = r"%(?P<Name>[A-Z][a-z]+)%[^|$%.]*<(?P<Product>\w+)>[^|$%.]*\|(?P<Quantity>\d+)\|[^|$%.\d]*(?P<Price>\d+\.?\d+)\$"
total = 0
while True:
    text = input()
    if "end of shift" in text:
        break
    results = re.finditer(pattern, text)
    for result in results:
        total += float(result.group("Price")) * int(result.group("Quantity"))
        print(f"{result.group('Name')}: {result.group('Product')} - {float(result.group('Price')) * float(result.group('Quantity')):.2f}")
print(f"Total income: {total:.2f}")