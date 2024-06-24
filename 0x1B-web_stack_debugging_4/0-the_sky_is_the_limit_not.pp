# This Puppet manifest increases the limits for Nginx to handle a higher load
exec { 'nginx fix':
  command  => "sed -i 's/-n 15/-n 4096/g' /etc/default/nginx && service nginx restart",
  onlyif   => 'test -e /etc/default/nginx',
  provider => 'shell',
}

# This ensures the exec command runs only if there is a change
exec { 'restart-nginx':
  command     => '/etc/init.d/nginx restart',
  subscribe   => Exec['nginx fix'],
  refreshonly => true,
}
