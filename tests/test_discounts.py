import pytest

from src.discounts import apply_discount


def test_apply_discount_no_discount():
    assert apply_discount(100, 0) == 100


def test_apply_discount_partial_discount():
    assert apply_discount(200, 25) == 150


def test_apply_discount_full_discount():
    assert apply_discount(100, 100) == 0


def test_apply_discount_raises_for_percent_over_100():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
