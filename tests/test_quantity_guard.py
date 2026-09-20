import pytest

from calc import Invoice
from calc.errors import InvalidLine


def test_rejects_zero_quantity():
    with pytest.raises(InvalidLine):
        Invoice("Acme").add(100, 0)


def test_guard_message_is_specific():
    try:
        Invoice("Acme").add(100, -1)
    except InvalidLine as exc:
        assert "quantity" in str(exc)
    else:
        raise AssertionError("expected InvalidLine")
