from __future__ import annotations

import pytest

from calc.invoice import Invoice


def test_invoice_add_rejects_non_positive_quantity() -> None:
    """Invoice.add rejects zero or negative quantities."""
    invoice = Invoice("Acme")

    with pytest.raises(ValueError):
        invoice.add(100, 0)

    with pytest.raises(ValueError):
        invoice.add(100, -2)
