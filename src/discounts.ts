export function applyDiscount(price: number, discount: number): number {
  return price - Math.abs(discount);
}
