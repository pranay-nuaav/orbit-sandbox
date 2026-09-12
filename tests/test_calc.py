from calc import Invoice, apply_discount, format_money, line_total


def test_apply_discount_reduces_amount():
    assert apply_discount(100, 10) == 90


def test_apply_discount_zero_is_identity():
    assert apply_discount(250, 0) == 250


def test_line_total_multiplies_then_discounts():
    assert line_total(50, 4, 10) == 180


def test_invoice_totals_its_lines():
    inv = Invoice("Acme").add(100, 2).add(50, 1)
    assert inv.total() == 250


def test_format_money_uses_currency_symbol():
    assert format_money(1234.5, "USD") == "$1,234.50"
    assert format_money(1234.5) == "₹1,234.50"
