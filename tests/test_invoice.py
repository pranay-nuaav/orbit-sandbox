import pytest

from calc.invoice import Invoice


def test_add_rejects_non_positive_quantity() -> None:
    """Invoice.add rejects zero or negative quantities while accepting positives."""
    invoice = Invoice("Acme")

    with pytest.raises(ValueError):
        invoice.add(100, 0)

    with pytest.raises(ValueError):
        invoice.add(100, -2)

    invoice.add(100, 2)
    assert invoice.total() == 200
