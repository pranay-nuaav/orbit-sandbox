def calculate_discounted_price(price, discount):
    if discount < 0:
        discount = 0
    return price - (price * discount / 100)
