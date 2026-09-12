"""Money formatting."""


def format_money(amount, currency="INR"):
    symbol = {"INR": "₹", "USD": "$", "GBP": "£"}.get(currency, "")
    return f"{symbol}{amount:,.2f}"
