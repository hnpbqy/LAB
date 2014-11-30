#!/usr/bin/env ruby
# -*- coding: utf-8 -*-
require 'open-uri'
File.open('./1.jpg', 'wb') {|f| f.write(open('http://tp1.sinaimg.cn/2264073420/180/40025028927/1') {|f1| f1.read})}
