#!/usr/bin/env ruby
#encoding: utf-8
arr = ['石头', '剪刀', '布']
win_arr = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
#随机computer的值，放入result数组中
result = [arr.sample]
while (true)
  puts "请输入石头、剪刀、布"
  input_value = gets.force_encoding("GBK").encode("UTF-8").chomp
  if arr.include? input_value
    result << input_value
    if result[0] == result[1]
      puts '平手'
    elsif win_arr.include? result
      puts '电脑获胜'
    else
      puts '您获胜了'
      break
    end
  else
    puts '输入的值有误，请输入石头、剪刀、布'
    next
  end
end


