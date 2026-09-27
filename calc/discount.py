def apply_discount(price, percent):
    if percent > 100:
        raise ValueError(f"discount percent {percent} is invalid")
    return price - (price * (percent / 100))
