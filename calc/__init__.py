"""A tiny invoicing helper. Small on purpose — the point is that the tests are real."""

from calc.discount import apply_discount
from calc.invoice import Invoice, line_total
from calc.money import format_money

__all__ = ["apply_discount", "Invoice", "line_total", "format_money"]
