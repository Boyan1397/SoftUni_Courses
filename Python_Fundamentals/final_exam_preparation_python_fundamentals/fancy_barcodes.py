import re

pattern = r"\@#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@#+"
number_pattern = r"\d"
n_lines = int(input())
for _ in range(n_lines):
    barcode = input()
    if re.match(pattern, barcode):
        results = re.findall(number_pattern, barcode)
        if not results:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(results)}")
    else:
        print("Invalid barcode")

