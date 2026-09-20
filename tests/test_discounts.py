import pytest

from app.discounts import apply_discount


def test_apply_discount_rejects_negative_and_over_100_percent():
    for percent in (-1, 101):
        with pytest.raises(ValueError):
            apply_discount(100, percent)
