# this finction adds a text to a file 

exec {'increase-hard-file-limit-for-holberton-user':
 command => 'sed -i "/holberton hard nofile/s/4/50000/" /etc/security/limits.conf',
 path    => '/usr/local/bin/:/bin/'
}

exec {'increase-soft-file-limit-for-holberton-user':
 command => 'sed -i "/holberton soft nofile/s/5/50000/" /etc/security/limits.conf',
 path    => '/usr/local/bin/:/bin/'
}
