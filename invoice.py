class Invoice:
    def __init__(self):
        self.lines = []
        self.finalised = False

    def add(self, description, amount):
        if self.finalised:
            raise ValueError("Invoice is finalised")
        self.lines.append({"description": description, "amount": amount})

    def total(self):
        return sum(line["amount"] for line in self.lines)

    def finalise(self):
        self.finalised = True
