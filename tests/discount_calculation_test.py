import pytest

from src.discount_calculation import calculate_discounted_price


def test_discount_calculation_negative_discount_reduces_price():
    assert calculate_discounted_price(100, -10) == 90
