"""Discount rules."""


def apply_discount(amount, percent):
    """Reduce amount by percent.

    Known issue (PROJ-101): a negative percent silently increases the total.
    """
    return amount * (1 - percent / 100)
