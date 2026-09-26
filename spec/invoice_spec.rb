require "invoice"
require "format_money"

RSpec.describe Invoice do
  it "defaults currency to INR" do
    invoice = Invoice.new(total: 100)
    expect(invoice.currency).to eq("INR")
  end

  it "stores the provided currency" do
    invoice = Invoice.new(total: 100, currency: "USD")
    expect(invoice.currency).to eq("USD")
  end

  it "formats totals using the invoice currency" do
    invoice = Invoice.new(total: 100, currency: "GBP")
    expect(invoice.formatted_total).to eq(format_money(100, "GBP"))
  end

  it "keeps current behavior for unknown currencies" do
    invoice = Invoice.new(total: 100, currency: "XYZ")
    expect(invoice.formatted_total).to eq(format_money(100, "XYZ"))
  end
end
