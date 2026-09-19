from dataclasses import dataclass

CURRENCY_SYMBOLS = {
    "INR": "₹",
    "USD": "$",
    "GBP": "£",
}


def format_money(amount, currency="INR"):
    symbol = CURRENCY_SYMBOLS.get(currency)
    if symbol:
        return f"{symbol}{amount:,.2f}"
    return f"{amount:,.2f} {currency}"


@dataclass
class LineItem:
    description: str
    quantity: int
    unit_price: float

    def total(self):
        return self.quantity * self.unit_price


class Invoice:
    def __init__(self, items, currency="INR"):
        self.items = items
        self.currency = currency

    def total(self):
        return sum(item.total() for item in self.items)

    def formatted_total(self):
        return format_money(self.total(), self.currency)
