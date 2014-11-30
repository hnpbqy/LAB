#!/usr/bin/env ruby
# -*- coding: utf-8 -*-
def rgb(red, green, blue)
  16 + (red * 36) + (green * 6) + blue
end
 
def gray(g)
  232 + g
end
 
def set_color(fg, bg)
  print "\x1b[38;5;#{fg}m" if fg
  print "\x1b[48;5;#{bg}m" if bg
end
 
def reset_color
  print "\x1b[0m"
end
 
def print_color(txt, fg, bg)
  set_color(fg, bg)
  print txt
  reset_color
end
 
# convenience method
def rgb_cube
  for green in 0..5 do
    0.upto 5 do |red|
      0.upto 5 do |blue|
        yield [red, green, blue]
      end
      print " "
    end
    puts
  end
end
 
# rgb list on black bg
rgb_cube do |red, green, blue|
  print_color("%d%d%d  " % [red, green, blue], rgb(red, green, blue), nil)
end
puts
 
# rgb list on white bg
rgb_cube do |red, green, blue|
  print_color("%d%d%d  " % [red, green, blue], rgb(red, green, blue), 15)
end
puts
 
# system palette:
print "System colors:\n";
(0..7).each do |color|
  print_color("  ", nil, color)
end
p
 
(8..15).each do |color|
  print_color("  ", nil, color)
end
p
p
 
# color cube
print "Color cube, 6x6x6:\n"
rgb_cube do |red, green, blue|
  print_color("  ", nil, rgb(red, green, blue))
end
puts
 
# grayscale ramp
print "Grayscale ramp:\n"
(0..23) .each do |g|
  print_color("  ", nil, gray(g))
end
 
p
p
