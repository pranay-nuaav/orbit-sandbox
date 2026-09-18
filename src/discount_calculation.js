function calculateTotal(price, discount) {
  const safeDiscount = discount < 0 ? 0 : discount;
  return price - (price * safeDiscount / 100);
}

module.exports = { calculateTotal };
