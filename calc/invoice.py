"""Invoice lines and totals."""

from dataclasses import dataclass, field

from calc.discount import apply_discount


def line_total(unit_price, quantity, discount_percent=0):
    return apply_discount(unit_price * quantity, discount_percent)


@dataclass
class Invoice:
    customer: str
    lines: list = field(default_factory=list)

    def add(self, unit_price, quantity, discount_percent=0):
        self.lines.append(line_total(unit_price, quantity, discount_percent))
        return self

    def total(self):
        return sum(self.lines)
