#!/usr/bin/env ruby
a = ARGV[0].scan(/\[(from|to|flags):(\+?\w+|[-?[0-1]:?]+)\]/)
from = a[0][1]
to = a[1][1]
flags = a[2][1]

puts from + "," + to + "," + flags