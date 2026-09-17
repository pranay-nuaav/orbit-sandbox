const { calculateDiscountedPrice } = require('../../src/discounts/discountCalculator');

describe('calculateDiscountedPrice', () => {
  it('does not increase price when given a negative discount', () => {
    const price = 100;
    const result = calculateDiscountedPrice(price, -10);
    expect(result).toBe(price);
  });
});
