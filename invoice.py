class Invoice:
    def __init__(self):
        self.lines = []
        self._finalised = False

    def add(self, description, amount):
        if self._finalised:
            raise ValueError("Cannot add lines to a finalised invoice")
        self.lines.append((description, amount))

    def total(self):
        return sum(amount for _, amount in self.lines)

    def finalise(self):
        self._finalised = True
