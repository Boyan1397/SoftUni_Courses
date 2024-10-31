from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.CAPACITY)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        # Base information
        store_info = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"

        # Estimated profit
        profit_info = self.get_estimated_profit()

        # Organize products by model
        product_details = {}
        for product in self.products:
            if product.model not in product_details:
                product_details[product.model] = {'count': 0, 'total_price': 0.0}
            product_details[product.model]['count'] += 1
            product_details[product.model]['total_price'] += product.price

        # Sort models alphabetically
        sorted_models = sorted(product_details.keys())

        # Prepare detailed product information
        product_info_lines = []
        for model in sorted_models:
            count = product_details[model]['count']
            avg_price = product_details[model]['total_price'] / count
            product_info_lines.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")

        # Combine all parts into the final output
        product_info = "\n".join(product_info_lines)
        stats = (
            f"{store_info}\n"
            f"{profit_info}\n"
            f"**Furniture for sale:\n"
            f"{product_info}"
        )
        return stats

