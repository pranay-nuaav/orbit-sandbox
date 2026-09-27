import pytest

from calc import apply_discount


def test_apply_discount_no_discount():
    assert apply_discount(100, 0) == 100


def test_apply_discount_half_off():
    assert apply_discount(200, 50) == 100


def test_apply_discount_full_discount():
    assert apply_discount(150, 100) == 0


def test_apply_discount_rejects_over_100_percent():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
