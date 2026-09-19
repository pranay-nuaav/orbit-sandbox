require "rails_helper"

RSpec.describe Invoice, type: :model do
  describe "#subtotal" do
    it "sums pre-discount line totals" do
      invoice = Invoice.new
      invoice.add(100, 0.2)
      invoice.add(50, 0.1)

      expect(invoice.subtotal).to eq(150)
      expect(invoice.total).to eq(125)
    end

    it "matches total when no discounts are applied" do
      invoice = Invoice.new
      invoice.add(100, 0)
      invoice.add(50, 0)

      expect(invoice.subtotal).to eq(invoice.total)
    end
  end
end
