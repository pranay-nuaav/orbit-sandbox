from dataclasses import dataclass


@dataclass
class LineItem:
    description: str
    amount: int


class Invoice:
    def __init__(self):
        self.lines = []
        self.finalised = False

    def add(self, description, amount):
        if self.finalised:
            raise RuntimeError("Invoice is finalised")
        self.lines.append(LineItem(description, amount))

    def total(self):
        return sum(line.amount for line in self.lines)

    def finalise(self):
        self.finalised = True
