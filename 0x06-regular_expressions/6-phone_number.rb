#!/usr/bin/env ruby
puts ARGV[0].scan(/\d{10}$(?![A-Za-z\s])/).join
