def apply_discount(amount, discount_percent):
    if discount_percent > 100:
        raise ValueError("Discount percent cannot exceed 100")
    return amount - (amount * discount_percent / 100)
