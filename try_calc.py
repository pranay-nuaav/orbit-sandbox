from calc import Invoice, apply_discount, format_money

inv = Invoice("Acme").add(1200, 2, 10).add(450, 1)
for i, line in enumerate(inv.lines, 1):
    print(f"line {i}: {format_money(line)}")
print("total  :", format_money(inv.total()))

print("\nPROJ-101:", format_money(apply_discount(100, -50)), "for a -50% 'discount' on ₹100")