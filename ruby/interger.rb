class Integer
  def reverse(a = 0)
    n = self
    while n > 0
      a = a * 10 + n % 10
      n /= 10
    end
    return a
  end

  def symmetrize(axis = false)
    reverse self / (axis ? 10 : 1)
  end

  def palindrome?
    self == reverse
  end

  def double
    self * self
  end
end

(1..10000).to_a.each do |i|
  [false, true].map {|axis|
    i.symmetrize(axis).double
  }.each {|n|
    puts n if n <= 10 ** 14 and n.palindrome?
  }
end
 