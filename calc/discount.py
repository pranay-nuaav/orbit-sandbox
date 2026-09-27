def apply_discount(amount, percent):
    if percent > 100:
        raise ValueError("percent must be <= 100")
    return amount - (amount * (percent / 100))
