#---
# Excerpted from "Agile Web Development with Rails, 4rd Ed.",
# published by The Pragmatic Bookshelf.
# Copyrights apply to this code. It may not be used to create training material, 
# courses, books, articles, and the like. Contact us if you are in doubt.
# We make no guarantees that this code is fit for any purpose. 
# Visit http://www.pragmaticprogrammer.com/titles/rails4 for more book information.
#---
class CreateDetails < ActiveRecord::Migration
  def self.up
    create_table :details do |t|
      t.integer :product_id
      t.string  :sku
      t.string  :manufacturer
    end
  end

  def self.down
    drop_table :details
  end
end
