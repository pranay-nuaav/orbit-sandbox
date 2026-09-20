from calc import Invoice


def test_subtotal_sums_lines():
    inv = Invoice("Acme").add(100, 2).add(50, 1)
    assert inv.subtotal() == 250


def test_total_with_tax_adds_rate():
    inv = Invoice("Acme").add(100, 1)
    assert inv.total_with_tax(18) == 118


def test_total_with_tax_zero_is_subtotal():
    inv = Invoice("Acme").add(200, 1)
    assert inv.total_with_tax(0) == 200
