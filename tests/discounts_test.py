import pytest

from src.discounts import apply_discount


def test_negative_discount_does_not_increase_total():
    total = 100
    assert apply_discount(total, -0.1) == pytest.approx(90)
