# -*- coding:utf-8-*-
require 'rubygems'
require 'open-uri'


url_hash = {}

open('http://www.cnblogs.com/TomXu/archive/2011/12/15/2288411.html').each do |i|
  if i =~ /(http:\/\/www.cnblogs.com\/TomXu\/archive.*\.html).*(.*">.*<\/a)/
    url_hash[$1] = $2[2..-4]
  end
end

url_hash.each do |k, v|
  # puts k
  # puts v
  # puts "**********************"
  `wget #{k} -O #{v}.html`
end