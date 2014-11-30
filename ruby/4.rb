#!/usr/bin/env ruby
#encoding: utf-8
t1 = Time.now.to_i
min = Math.sqrt(1).to_i
max = Math.sqrt(10**14).to_i
 
def isH(num)
  num = num.to_s
  return  num == num.reverse
end
 
for num in (min..max)
  if isH num
    z = num**2
    if isH z
      puts z
    end
  end
end
t2 = Time.now.to_i
puts t2-t1
