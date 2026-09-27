class Invoice:
    def __init__(self):
        self.lines = []

    def add(self, unit_price, quantity, discount_rate=0):
        line_total = unit_price * quantity * (1 - discount_rate)
        self.lines.append(
            {
                "unit_price": unit_price,
                "quantity": quantity,
                "discount_rate": discount_rate,
                "total": line_total,
            }
        )

    def remove(self, position):
        if position < 0 or position >= len(self.lines):
            raise IndexError("Line position out of range")
        self.lines.pop(position)

    def total(self):
        return sum(line["total"] for line in self.lines)
