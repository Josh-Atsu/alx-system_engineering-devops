#!/usr/bin/env ruby

sender, receiver, flags =  ARGV[0].scan(/\[(?:from|to|flags):(\S+?)\]/).flatten
puts "#{sender},#{receiver},#{flags}"
