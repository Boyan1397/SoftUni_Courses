list_products = input().split(": ")
products_dict = {}

while list_products[0] != "statistics":
    product_key = list_products[0]
    quantity = int(list_products[1])
    if product_key in products_dict:
        products_dict[product_key] += quantity
    else:
        products_dict[product_key] = quantity
    list_products = input().split(": ")

print("Products in stock:")
total = 0
for key, value in products_dict.items():
    total += value
    print(f"- {key}: {value}")
print(f"Total Products: {len(products_dict)}")
print(f"Total Quantity: {total}")