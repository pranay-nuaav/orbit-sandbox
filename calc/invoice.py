from __future__ import annotations

from typing import List, Tuple


def line_total(price: float, quantity: int, discount: float = 0) -> float:
    total = price * quantity
    if discount:
        total -= total * (discount / 100)
    return total


class Invoice:
    def __init__(self, customer: str) -> None:
        self.customer = customer
        self.lines: List[Tuple[float, int, float]] = []

    def add(self, price: float, quantity: int, discount: float = 0) -> "Invoice":
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.lines.append((price, quantity, discount))
        return self

    def total(self) -> float:
        return sum(
            line_total(price, quantity, discount)
            for price, quantity, discount in self.lines
        )


__all__ = ["line_total", "Invoice"]
