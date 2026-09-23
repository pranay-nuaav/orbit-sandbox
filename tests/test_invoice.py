import pytest

from invoice import Invoice


def test_invoice_finalised_add_raises_and_total_works():
    invoice = Invoice()
    invoice.add("widget", 10)
    invoice.finalise()
    assert invoice.total() == 10
    with pytest.raises(ValueError):
        invoice.add("another", 5)
