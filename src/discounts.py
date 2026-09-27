def apply_discount(price, discount_percent):
    if discount_percent > 100:
        raise ValueError("discount percent cannot exceed 100")
    return price - (price * discount_percent / 100)
