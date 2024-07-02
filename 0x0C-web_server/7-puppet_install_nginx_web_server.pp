# Puppet manifest to setup Nginx server

# Ensure that the Nginx package is installed
package { 'nginx':
  ensure => 'installed',
}

# Create or overwrite the index.html file with specific content
file { '/var/www/html/index.html':
  content => 'Holberton School',
}

# Add a rewrite rule to redirect /redirect_me to a YouTube video
file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# Ensure that the Nginx service is running and requires the Nginx package
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
