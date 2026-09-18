CURRENCY_SYMBOLS = {
    "INR": "₹",
    "USD": "$",
    "GBP": "£",
}


def format_money(amount, currency="INR"):
    symbol = CURRENCY_SYMBOLS.get(currency)
    if symbol:
        return f"{symbol}{amount:.2f}"
    return f"{amount:.2f}"


class Invoice:
    def __init__(self, line_items, currency="INR"):
        self.line_items = line_items
        self.currency = currency

    def total(self):
        return sum(item.total for item in self.line_items)

    def formatted_total(self):
        return format_money(self.total(), self.currency)
