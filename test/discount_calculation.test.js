const { calculateTotal } = require('../src/discount_calculation');

describe('discount calculation', () => {
  it('applies percent discount', () => {
    expect(calculateTotal(100, 10)).toBe(90);
  });

  it('does not increase price for negative discount', () => {
    expect(calculateTotal(100, -10)).toBe(100);
  });
});
