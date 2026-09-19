import pytest
from invoice import Invoice


def test_invoice_can_be_finalised_and_total_still_works():
    invoice = Invoice()
    invoice.add("item", 10)
    invoice.add("item", 5)

    invoice.finalise()

    assert invoice.total() == 15


def test_add_raises_after_finalise_and_works_before():
    invoice = Invoice()
    invoice.add("item", 10)

    invoice.finalise()

    with pytest.raises(ValueError):
        invoice.add("item", 5)
