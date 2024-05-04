list_of_products = input().split()
products = {}
for index in range(0, len(list_of_products), 2):
    products_key = list_of_products[index]
    quantity = int(list_of_products[index +1])
    products[products_key] = quantity
print(products)
