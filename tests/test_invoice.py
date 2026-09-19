from invoice import Invoice, LineItem, format_money


def test_invoice_defaults_currency_to_inr_when_not_provided():
    invoice = Invoice([LineItem("Consulting", 1, 1000)])
    assert invoice.currency == "INR"


def test_invoice_total_format_uses_invoice_currency_and_unknown_code_behavior():
    items = [LineItem("Consulting", 1, 1000)]
    gbp_invoice = Invoice(items, currency="GBP")
    assert gbp_invoice.formatted_total() == format_money(gbp_invoice.total(), "GBP")

    unknown_invoice = Invoice(items, currency="ZZZ")
    assert unknown_invoice.formatted_total() == format_money(unknown_invoice.total(), "ZZZ")
