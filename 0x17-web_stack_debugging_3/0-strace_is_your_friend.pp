# fixing the typo error in "wp-settings.php"

exec {'Fix-WordPressing-Error':
command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
path    => '/usr/local/bin/:/bin/'
}
