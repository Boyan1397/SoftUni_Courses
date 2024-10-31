from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    PRODUCT_TYPES = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    STORE_TYPES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.PRODUCT_TYPES:
            raise Exception("Invalid product type!")

        product = FactoryManager.PRODUCT_TYPES[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.STORE_TYPES:
            raise Exception(f"{store_type} is an invalid type of store!")

        store = FactoryManager.STORE_TYPES[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        acceptable_sub_type = 'Furniture' if store.store_type == 'FurnitureStore' else 'Toys'
        matching_products = [p for p in products if p.sub_type == acceptable_sub_type]

        if not matching_products:
            return "Products do not match in type. Nothing sold."

        store.products.extend(matching_products)
        store.capacity -= len(matching_products)

        total_price = sum(p.price for p in matching_products)
        self.income += total_price

        for product in matching_products:
            self.products.remove(product)

        return f"Store {store.name} successfully purchased {len(matching_products)} items."

    def unregister_store(self, store_name: str):
        store_to_remove = None
        for s in self.stores:
            if s.name == store_name:
                store_to_remove = s
                break

        if store_to_remove is None:
            return "No such store!"

        if store_to_remove.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store_to_remove)
        return f"Successfully unregistered store {store_name}, location: {store_to_remove.location}."

    def discount_products(self, product_model: str):
        # Filter unsold products by the given model
        products_to_discount = [p for p in self.products if p.model == product_model]

        # Initialize the count of discounted products
        discount_count = 0

        for product in products_to_discount:
            if product.sub_type == "Furniture":
                # Apply 10% discount for Furniture products
                product.discount()  # Assuming discount() method is defined in product classes
                discount_count += 1
            elif product.sub_type == "Toys":
                # Apply 20% discount for Toys products
                product.discount()  # Assuming discount() method is defined in product classes
                discount_count += 1

        return f"Discount applied to {discount_count} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store_list = [s for s in self.stores if s.name == store_name]
        if not store_list:
            return "There is no store registered under this name!"
        else:
            store = store_list[0]
            return store.store_stats()

    def statistics(self):
        # Calculate unsold products and their total net price
        products_summary = {}
        total_products_price = 0.0

        for product in self.products:
            if product.sub_type == 'Furniture' or product.sub_type == 'Toys':
                if product.model not in products_summary:
                    products_summary[product.model] = 0
                products_summary[product.model] += 1
                total_products_price += product.price

        # Generate product statistics
        product_statistics_lines = []
        for model in sorted(products_summary.keys()):
            count = products_summary[model]
            product_statistics_lines.append(f"{model}: {count}")

        # Generate store statistics
        store_statistics_lines = sorted([store.name for store in self.stores])

        # Format the results
        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {total_products_price:.2f}",
            "\n".join(product_statistics_lines),
            f"***Partner Stores: {len(self.stores)}***",
            "\n".join(store_statistics_lines)
        ]

        return "\n".join(result)
