import pytest

from invoice import Invoice


def test_add_rejects_non_positive_quantity():
    invoice = Invoice("Acme")

    with pytest.raises(ValueError):
        invoice.add(100, -2)

    with pytest.raises(ValueError):
        invoice.add(100, 0)
