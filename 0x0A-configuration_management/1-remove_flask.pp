#remove flask
exec { 'remove_flask':
  command => '/usr/bin/pip3 uninstall -y flask',
  path    => ['/usr/bin', '/usr/sbin'],
  onlyif  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}

package { 'python3-pip':
  ensure => absent,
}
