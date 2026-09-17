class Invoice
  Line = Struct.new(:name, :quantity, :price, :discount, :total, :subtotal)

  def initialize
    @lines = []
  end

  def add(name, quantity, price, discount = 0)
    total = line_total(quantity, price, discount)
    subtotal = quantity * price
    @lines << Line.new(name, quantity, price, discount, total, subtotal)
  end

  def total
    @lines.sum(&:total)
  end

  def subtotal
    @lines.sum(&:subtotal)
  end

  private

  def line_total(quantity, price, discount)
    quantity * price * (1 - discount)
  end
end
