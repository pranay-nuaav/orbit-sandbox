from invoice import Invoice, format_money


def test_invoice_total_formats_with_invoice_currency_and_default_inr():
    amount = 1234.5
    invoice_default = Invoice(amount)
    assert invoice_default.formatted_total() == format_money(amount, "INR")

    invoice_gbp = Invoice(amount, currency="GBP")
    assert invoice_gbp.formatted_total() == format_money(amount, "GBP")

    invoice_unknown = Invoice(amount, currency="ZZZ")
    assert invoice_unknown.formatted_total() == format_money(amount, "ZZZ")
