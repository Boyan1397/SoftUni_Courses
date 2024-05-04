list_of_products = input().split()
products = {}
searched_products = input().split()
for index in range(0, len(list_of_products), 2):
    products_key = list_of_products[index]
    quantity = int(list_of_products[index +1])
    products[products_key] = quantity


for searched_product in searched_products:
    if searched_product in products.keys():
        print(f"We have {products[searched_product]} of {searched_product} left")
    else:
        print(f"Sorry, we don't have {searched_product}")