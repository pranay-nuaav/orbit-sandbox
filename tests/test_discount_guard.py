import pytest

from calc import apply_discount


def test_rejects_negative_percent():
    with pytest.raises(ValueError):
        apply_discount(100, -10)


def test_rejects_percent_above_100():
    with pytest.raises(ValueError):
        apply_discount(100, 120)


def test_valid_percent_still_works():
    assert apply_discount(100, 10) == 90
