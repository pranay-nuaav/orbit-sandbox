import pytest

from invoice import Invoice


def test_invoice_remove_line_updates_total():
    invoice = Invoice()
    invoice.add(10, 2, 0.1)
    invoice.add(5, 1, 0)
    invoice.add(3, 3, 0)

    assert invoice.total() == 32

    invoice.remove(1)

    assert invoice.total() == 27


def test_invoice_remove_invalid_position_raises():
    invoice = Invoice()
    invoice.add(10, 1, 0)
    total_before = invoice.total()

    with pytest.raises(IndexError, match="Line position out of range"):
        invoice.remove(2)

    assert invoice.total() == total_before
