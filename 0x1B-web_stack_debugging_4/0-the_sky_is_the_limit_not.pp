# fix ngix to accept and more services requests

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->
# And restart

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
