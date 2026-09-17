function calculateDiscountedPrice(price, discount) {
  if (discount < 0) {
    return price;
  }
  return price - (price * discount) / 100;
}

module.exports = { calculateDiscountedPrice };
