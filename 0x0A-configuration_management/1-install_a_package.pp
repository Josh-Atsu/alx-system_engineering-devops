#!/usr/bin/pup
# creating a packege

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
