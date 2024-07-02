# install a package
package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/usr/sbin'],
  require => Package['python3-pip'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
