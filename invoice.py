def format_money(amount, currency="INR"):
    symbols = {"INR": "₹", "USD": "$", "GBP": "£"}
    symbol = symbols.get(currency)
    if symbol:
        return f"{symbol}{amount:.2f}"
    return f"{amount:.2f} {currency}"


class Invoice:
    def __init__(self, total, currency="INR"):
        self.total = total
        self.currency = currency

    def formatted_total(self, currency=None):
        if currency is None:
            currency = self.currency
        return format_money(self.total, currency)
