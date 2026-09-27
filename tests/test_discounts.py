import pytest

from src.discounts import apply_discount


def test_apply_discount_rejects_percent_above_100():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
