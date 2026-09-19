class Invoice < ApplicationRecord
  has_many :line_items

  def add(amount, discount = 0)
    line_item = line_items.build
    line_item.total = line_item.line_total(amount, discount)
    line_items << line_item
  end

  def total
    line_items.sum(&:total)
  end

  def subtotal
    line_items.sum { |line_item| line_item.pre_discount_total || line_item.total }
  end
end

class LineItem < ApplicationRecord
  belongs_to :invoice

  attr_accessor :pre_discount_total

  def line_total(amount, discount = 0)
    self.pre_discount_total = amount
    amount - (amount * discount)
  end
end
