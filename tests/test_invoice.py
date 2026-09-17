import pytest

from src.invoice import Invoice, InvoiceLine


def test_invoice_can_be_finalised_and_total_still_works():
    invoice = Invoice()
    invoice.add(InvoiceLine("apple", 1, 2))
    invoice.finalise()
    assert invoice.total() == 2


def test_add_raises_after_finalised_and_behaves_before():
    invoice = Invoice()
    invoice.add(InvoiceLine("apple", 1, 2))
    invoice.finalise()
    with pytest.raises(RuntimeError):
        invoice.add(InvoiceLine("banana", 2, 3))

    invoice2 = Invoice()
    invoice2.add(InvoiceLine("apple", 1, 2))
    invoice2.add(InvoiceLine("banana", 2, 3))
    assert invoice2.total() == 8
