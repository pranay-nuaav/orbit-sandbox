def effective_discount_percent(discount_percent, quantity):
    if quantity >= 100:
        discount_percent += 5
    return min(discount_percent, 50)
