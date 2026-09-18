import pytest

from invoice import Invoice, format_money


def test_invoice_defaults_currency_inr():
    invoice = Invoice([])
    assert invoice.currency == "INR"


def test_invoice_formats_total_with_invoice_currency():
    invoice = Invoice([], currency="GBP")
    assert invoice.formatted_total() == format_money(invoice.total(), "GBP")


def test_invoice_formats_total_with_unknown_currency_behaves_same():
    invoice = Invoice([], currency="XYZ")
    assert invoice.formatted_total() == format_money(invoice.total(), "XYZ")
