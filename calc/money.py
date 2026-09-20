"""Money formatting."""

from decimal import ROUND_HALF_UP, Decimal


def format_money(amount, currency="INR"):
    """Format an amount for display.

    Rounds half up at two places rather than relying on float formatting, which
    rounds 2.675 down because the binary representation is slightly below it.
    Arithmetic stays exact; only the displayed value is rounded.
    """
    symbol = {"INR": "\u20b9", "USD": "$", "GBP": "\u00a3"}.get(currency, "")
    rounded = Decimal(str(amount)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{symbol}{rounded:,.2f}"
