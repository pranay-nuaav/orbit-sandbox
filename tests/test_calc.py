import pytest

from calc import apply_discount


def test_apply_discount():
    assert apply_discount(100, 10) == 90


def test_apply_discount_full():
    assert apply_discount(100, 100) == 0


def test_apply_discount_rejects_percent_above_100():
    with pytest.raises(ValueError) as excinfo:
        apply_discount(100, 150)
    assert "150" in str(excinfo.value)
