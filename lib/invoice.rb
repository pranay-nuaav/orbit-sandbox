require "format_money"

class Invoice
  attr_reader :total, :currency

  def initialize(total:, currency: "INR")
    @total = total
    @currency = currency
  end

  def formatted_total
    format_money(total, currency)
  end
end
