def apply_discount(total, discount):
    if discount < 0:
        discount = abs(discount)
    return total - (total * discount)
