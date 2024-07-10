# Installation and running nginx

# updating packages
exec { 'update_package_list':
  command => 'usr/bin/apt-get update',
  path    => ['/usr/bin', '/usr/sbin'],
}

# install nginx packege
package { 'nginx':
  ensure   => installed,
  required => Exec['update_package_list'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Package['nginx']
}

