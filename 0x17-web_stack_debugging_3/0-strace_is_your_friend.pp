nx ULIMIT setting to handle more file descriptors
exec { 'increase-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart the Nginx service to apply the updated ULIMIT setting
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
