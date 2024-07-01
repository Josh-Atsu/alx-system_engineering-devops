#define a puppet file

$public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDX5h5t301xYjTlNDGzs5gqn3YHNSuJPFDxrJZ7HSdb/GId8Qh63YQiRkQT3h9EULEf1LgmXnz2ZH62nsFXBBNfMqrIVI3NJFb7eTNWBvCuwlNlxGN7n72dTuRRllj041LtUjgmNkRrWXb7iEodWmY9Zjr65kk3gMJe2I1gSvES58nottrCo7OaDnaI9i0fcKBLYyn6Zk9GnhxW4pDOMiZ31nTRqXYOoecy8HgUcVqj3EwCuljoLXXibCQWn6qm9nPO9wmfZb7gnEjQY8UcO9/Qw7TbklRJe3n/3PbUTcKLzaX2f85QeCGpoBXqR2iVw/iIamo08588fUH4t+cF08qAOunoApzJyOwjI0XMJR7KtvKtgzSLFwwKTDX0hBb0V2uYXnw7nvKZJrShlzKiVvYgpNYDSJ1jhdUnpCRmArW11pBRnmGV5AvK9kSUyimPnHLO4P7YFe1wrFIs3ZTPbDBIidmZmfphLOJL4tGZ1R39sLphFEwu+6/01jQqWBIGyZk= root@f3c0cd66e598"

file { '/root/.ssh/':
	ensure => directory,
	owner => 'root',
	group => 'root',
	mode => 0700,
}

file { '/root/.ssh/authorized_key':
	ensure => present,
	owner => 'root',
	group => 'root',
	mode => 0600,
	content => $public_key,
}
