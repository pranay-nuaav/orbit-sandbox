"""Discount rules."""


def apply_discount(amount, percent):
    """Reduce amount by percent.

    Raises ValueError if percent is outside 0-100. A negative percent used to
    silently increase the total, which overcharged the customer on a typo.
    """
    if percent < 0 or percent > 100:
        raise ValueError(f"discount percent must be between 0 and 100, got {percent}")
    return amount * (1 - percent / 100)
