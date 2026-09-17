class Invoice:
    def __init__(self, customer):
        self.customer = customer
        self.lines = []

    def add(self, price, quantity):
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.lines.append(price * quantity)

    def total(self):
        return sum(self.lines)
