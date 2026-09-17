import pytest

from app.services.discount_calculator import calculate_discounted_price


def test_negative_discount_does_not_increase_price():
    original_price = 100
    discounted_price = calculate_discounted_price(original_price, -10)
    assert discounted_price == original_price
