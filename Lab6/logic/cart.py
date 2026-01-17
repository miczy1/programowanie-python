class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def total_price(self):
        return sum(product.price for product in self.products)

    def __len__(self):
        return len(self.products)

    def __contains__(self, product):
        return product in self.products

    def __str__(self):
        if not self.products:
            return "Koszyk jest pusty."

        lines = ["Zawartość koszyka:"]
        for product in self.products:
            lines.append(str(product))
        lines.append(f"Łączna cena: {self.total_price():.2f} zł")
        return "\n".join(lines)
