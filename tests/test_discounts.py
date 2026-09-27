from pricing import discounts


def test_bulk_discount_applies_for_quantity_at_or_above_100_and_caps_at_50_percent():
    assert discounts.effective_discount_percent(quantity=100, discount_percent=10) == 15
    assert discounts.effective_discount_percent(quantity=150, discount_percent=48) == 50
