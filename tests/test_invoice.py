import pytest

from invoice import Invoice


def test_invoice_finalised_prevents_add_and_allows_total():
    invoice = Invoice()
    invoice.add("widget", 10)
    invoice.finalise()

    assert invoice.total() == 10

    with pytest.raises(RuntimeError):
        invoice.add("extra", 5)

    invoice2 = Invoice()
    invoice2.add("widget", 10)
    invoice2.add("extra", 5)
    assert invoice2.total() == 15
