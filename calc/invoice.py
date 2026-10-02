from __future__ import annotations

from decimal import Decimal


def _to_decimal(value) -> Decimal:
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def line_total(price, quantity, discount=0):
    price_d = _to_decimal(price)
    quantity_d = _to_decimal(quantity)
    discount_d = _to_decimal(discount)
    subtotal = price_d * quantity_d
    if discount_d:
        subtotal = subtotal * (Decimal("100") - discount_d) / Decimal("100")
    return subtotal


class Invoice:
    def __init__(self, customer: str):
        self.customer = customer
        self._lines = []

    def add(self, price, quantity, discount=0):
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self._lines.append((_to_decimal(price), _to_decimal(quantity), _to_decimal(discount)))
        return self

    def total(self):
        total = Decimal("0")
        for price, quantity, discount in self._lines:
            total += line_total(price, quantity, discount)
        return total
