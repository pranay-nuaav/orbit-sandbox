def apply_discount(amount, percent):
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return amount - (amount * percent / 100)
