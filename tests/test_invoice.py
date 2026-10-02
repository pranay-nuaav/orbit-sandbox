import pytest

from calc.invoice import Invoice


def test_invoice_add_rejects_non_positive_quantity() -> None:
    """Invoice.add rejects non-positive quantities."""
    invoice = Invoice("Acme")

    with pytest.raises(ValueError):
        invoice.add(100, -2)

    with pytest.raises(ValueError):
        invoice.add(100, 0)

    invoice.add(100, 2)

    assert invoice.total() == 200
