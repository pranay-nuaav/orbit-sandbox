# lib/invoice.rb
class Invoice
  def initialize
    @lines = []
  end

  def add(line_item)
    @lines << { total: line_item.line_total, subtotal: line_item.subtotal }
  end

  def total
    @lines.sum { |line| line[:total] }
  end

  def subtotal
    @lines.sum { |line| line[:subtotal] }
  end
end

# lib/line_item.rb
class LineItem
  attr_reader :name, :unit_price, :quantity, :discount

  def initialize(name:, unit_price:, quantity: 1, discount: 0)
    @name = name
    @unit_price = unit_price
    @quantity = quantity
    @discount = discount
  end

  def line_total
    subtotal - (subtotal * discount)
  end

  def subtotal
    unit_price * quantity
  end
end
