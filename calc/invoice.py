from __future__ import annotations

from typing import Any, Iterable, List, Tuple, Optional


def line_total(unit_price: float, quantity: int = 1, discount: float = 0.0) -> float:
    subtotal = float(unit_price) * int(quantity)
    if discount:
        subtotal *= (100.0 - float(discount)) / 100.0
    return subtotal


class Invoice:
    def __init__(
        self,
        customer: Any = "",
        items: Optional[Iterable[Any]] = None,
        discount: float = 0.0,
    ) -> None:
        if items is None and not isinstance(customer, str):
            items = customer
            customer = ""
        self.customer = str(customer)
        self.items: List[Tuple[str, float, int]] = []
        self.discount = float(discount)
        if items:
            for item in items:
                self.items.append(self._normalize_item(item))

    def _normalize_item(self, item: Any) -> Tuple[str, float, int]:
        if isinstance(item, dict):
            description = item.get("description") or item.get("name") or ""
            unit_price = item.get("unit_price", item.get("price"))
            quantity = item.get("quantity", 1)
            if unit_price is None:
                raise ValueError("unit_price is required")
            return (str(description), float(unit_price), int(quantity))
        if isinstance(item, (list, tuple)):
            if len(item) == 3:
                description, unit_price, quantity = item
            elif len(item) == 2:
                description, unit_price = item
                quantity = 1
            else:
                raise ValueError("line item must have 2 or 3 elements")
            return (str(description), float(unit_price), int(quantity))
        description = getattr(item, "description", getattr(item, "name", ""))
        unit_price = getattr(item, "unit_price", getattr(item, "price", None))
        quantity = getattr(item, "quantity", 1)
        if unit_price is None:
            raise ValueError("unit_price is required")
        return (str(description), float(unit_price), int(quantity))

    def add(self, unit_price: float, quantity: int = 1, description: str = "") -> "Invoice":
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.items.append((str(description), float(unit_price), int(quantity)))
        return self

    def total(self) -> float:
        total = sum(line_total(price, qty) for _, price, qty in self.items)
        if self.discount:
            total *= (100.0 - self.discount) / 100.0
        return total
