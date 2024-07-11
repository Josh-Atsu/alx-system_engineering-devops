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

file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!",
}

exec { 'redirect_me':
  command  => 'sudo sed -i "53i \\\n\tlocation /redirect_me {\n\t\treturn 301 https://youtu.be/3NPZ-VKoa9Q?si=ewsZuSenvTqyJs3P;\n\t}\n" /etc/nginx/sites-available/default',
  provider => 'shell',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}
