require "minitest/autorun"
require_relative "../lib/invoice"

class InvoiceTest < Minitest::Test
  def test_subtotal_is_pre_discount_sum_and_total_unchanged
    invoice = Invoice.new
    invoice.add("widget", 2, 10, 0.1) # 2 * 10 = 20, 10% discount => 18
    assert_equal 20, invoice.subtotal
    assert_equal 18, invoice.total
  end

  def test_subtotal_equals_total_when_no_discount
    invoice = Invoice.new
    invoice.add("widget", 3, 5) # 3 * 5 = 15, no discount
    assert_equal 15, invoice.subtotal
    assert_equal 15, invoice.total
  end
end
