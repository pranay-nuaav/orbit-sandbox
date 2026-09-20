from calc import format_money


def test_half_up_at_two_places():
    assert format_money(2.675, "USD") == "$2.68"


def test_existing_formatting_unchanged():
    assert format_money(1234.5, "USD") == "$1,234.50"
