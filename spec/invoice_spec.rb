require "invoice"
require "line_item"

RSpec.describe Invoice do
  describe "#subtotal" do
    it "sums line amounts before discount and keeps total unchanged" do
      invoice = Invoice.new
      invoice.add(LineItem.new(name: "Widget", unit_price: 10, quantity: 2, discount: 0.1))
      invoice.add(LineItem.new(name: "Gadget", unit_price: 5, quantity: 1, discount: 0))

      expect(invoice.subtotal).to eq(25)
      expect(invoice.total).to eq(23)
    end

    it "equals total when there are no discounts" do
      invoice = Invoice.new
      invoice.add(LineItem.new(name: "Widget", unit_price: 10, quantity: 2, discount: 0))

      expect(invoice.subtotal).to eq(invoice.total)
    end
  end
end
