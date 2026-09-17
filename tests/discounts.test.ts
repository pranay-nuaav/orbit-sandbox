import { applyDiscount } from "../src/discounts";

describe("discount calculation", () => {
  it("discount_calculation_rejects_or_absorbs_negative_values", () => {
    expect(applyDiscount(100, -10)).toBe(90);
  });
});
