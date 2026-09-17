from dataclasses import dataclass


@dataclass
class InvoiceLine:
    description: str
    quantity: int
    price: int

    def total(self) -> int:
        return self.quantity * self.price


class Invoice:
    def __init__(self) -> None:
        self._lines: list[InvoiceLine] = []
        self._finalised = False

    def finalise(self) -> None:
        self._finalised = True

    def add(self, line: InvoiceLine) -> None:
        if self._finalised:
            raise RuntimeError("Invoice is finalised")
        self._lines.append(line)

    def total(self) -> int:
        return sum(line.total() for line in self._lines)
